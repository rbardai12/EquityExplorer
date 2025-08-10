#!/usr/bin/env python3
"""
Flask web application for EquityExplorer frontend
"""

import os
import json
import logging
from pathlib import Path
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for
from flask_cors import CORS
import pandas as pd

# Import EquityExplorer components
import sys
sys.path.append('..')
from src.equity_explorer import EquityExplorer
from config import Config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Global explorer instance
explorer = None

def get_explorer():
    """Get or create EquityExplorer instance"""
    global explorer
    if explorer is None:
        try:
            explorer = EquityExplorer()
        except Exception as e:
            logger.error(f"Failed to initialize EquityExplorer: {e}")
            return None
    return explorer

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/api/status')
def get_status():
    """Get system status"""
    try:
        explorer = get_explorer()
        if explorer is None:
            return jsonify({
                'status': 'error',
                'message': 'Failed to initialize EquityExplorer'
            })
        
        # Check if output directory exists and has files
        output_dir = Config.OUTPUT_DIR
        if output_dir.exists():
            csv_files = list(output_dir.glob('*.csv'))
            latest_files = []
            
            for file in csv_files[-10:]:  # Get 10 most recent files
                stat = file.stat()
                latest_files.append({
                    'name': file.name,
                    'size': stat.st_size,
                    'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    'type': 'csv'
                })
        else:
            latest_files = []
        
        return jsonify({
            'status': 'success',
            'explorer_ready': True,
            'output_directory': str(output_dir),
            'latest_files': latest_files,
            'config_ready': True
        })
        
    except Exception as e:
        logger.error(f"Error getting status: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

@app.route('/api/tickers')
def get_tickers():
    """Get available tickers from configuration"""
    try:
        return jsonify({
            'status': 'success',
            'tickers': Config.DEFAULT_STOCKS
        })
    except Exception as e:
        logger.error(f"Error getting tickers: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

@app.route('/api/process-ticker', methods=['POST'])
def process_ticker():
    """Process a single ticker"""
    try:
        data = request.get_json()
        ticker = data.get('ticker', '').upper()
        
        if not ticker:
            return jsonify({
                'status': 'error',
                'message': 'Ticker symbol is required'
            })
        
        explorer = get_explorer()
        if explorer is None:
            return jsonify({
                'status': 'error',
                'message': 'EquityExplorer not initialized'
            })
        
        # Process the ticker
        results = explorer.run_single_ticker_analysis(ticker)
        
        if results:
            return jsonify({
                'status': 'success',
                'message': f'Successfully processed {ticker}',
                'results': {
                    'ticker': ticker,
                    'statements': list(results.keys()),
                    'files': {k: str(v) for k, v in results.items()}
                }
            })
        else:
            return jsonify({
                'status': 'error',
                'message': f'Failed to process {ticker}'
            })
            
    except Exception as e:
        logger.error(f"Error processing ticker: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

@app.route('/api/process-tickers', methods=['POST'])
def process_tickers():
    """Process multiple tickers"""
    try:
        data = request.get_json()
        tickers = [t.upper() for t in data.get('tickers', [])]
        
        if not tickers:
            return jsonify({
                'status': 'error',
                'message': 'Ticker symbols are required'
            })
        
        explorer = get_explorer()
        if explorer is None:
            return jsonify({
                'status': 'error',
                'message': 'EquityExplorer not initialized'
            })
        
        # Process the tickers
        results = explorer.process_multiple_tickers(tickers)
        
        success_count = len([r for r in results.values() if r])
        
        return jsonify({
            'status': 'success',
            'message': f'Processed {success_count}/{len(tickers)} tickers successfully',
            'results': {
                'total': len(tickers),
                'successful': success_count,
                'failed': len(tickers) - success_count,
                'details': {
                    ticker: {
                        'success': bool(result),
                        'statements': list(result.keys()) if result else []
                    }
                    for ticker, result in results.items()
                }
            }
        })
        
    except Exception as e:
        logger.error(f"Error processing tickers: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

@app.route('/api/files')
def get_files():
    """Get list of available files"""
    try:
        output_dir = Config.OUTPUT_DIR
        if not output_dir.exists():
            return jsonify({
                'status': 'success',
                'files': []
            })
        
        files = []
        for file_path in output_dir.glob('*.csv'):
            stat = file_path.stat()
            files.append({
                'name': file_path.name,
                'path': str(file_path),
                'size': stat.st_size,
                'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                'type': 'csv'
            })
        
        # Sort by modification time (newest first)
        files.sort(key=lambda x: x['modified'], reverse=True)
        
        return jsonify({
            'status': 'success',
            'files': files
        })
        
    except Exception as e:
        logger.error(f"Error getting files: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

@app.route('/api/files/<filename>')
def get_file_content(filename):
    """Get content of a specific file"""
    try:
        file_path = Config.OUTPUT_DIR / filename
        
        if not file_path.exists():
            return jsonify({
                'status': 'error',
                'message': 'File not found'
            })
        
        # Read CSV file
        df = pd.read_csv(file_path)
        
        # Convert to JSON-serializable format
        data = {
            'columns': df.columns.tolist(),
            'rows': df.values.tolist(),
            'shape': df.shape,
            'info': {
                'filename': filename,
                'size': file_path.stat().st_size,
                'modified': datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
            }
        }
        
        return jsonify({
            'status': 'success',
            'data': data
        })
        
    except Exception as e:
        logger.error(f"Error reading file {filename}: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

@app.route('/api/download/<filename>')
def download_file(filename):
    """Download a file"""
    try:
        file_path = Config.OUTPUT_DIR / filename
        
        if not file_path.exists():
            return jsonify({
                'status': 'error',
                'message': 'File not found'
            })
        
        return send_file(
            file_path,
            as_attachment=True,
            download_name=filename,
            mimetype='text/csv'
        )
        
    except Exception as e:
        logger.error(f"Error downloading file {filename}: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

@app.route('/api/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    """Delete a file"""
    try:
        file_path = Config.OUTPUT_DIR / filename
        
        if not file_path.exists():
            return jsonify({
                'status': 'error',
                'message': 'File not found'
            })
        
        file_path.unlink()
        
        return jsonify({
            'status': 'success',
            'message': f'File {filename} deleted successfully'
        })
        
    except Exception as e:
        logger.error(f"Error deleting file {filename}: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

@app.route('/api/run-full-analysis', methods=['POST'])
def run_full_analysis():
    """Run full analysis with default stocks"""
    try:
        explorer = get_explorer()
        if explorer is None:
            return jsonify({
                'status': 'error',
                'message': 'EquityExplorer not initialized'
            })
        
        # Run full analysis
        results = explorer.run_full_analysis()
        
        success_count = len([r for r in results.values() if r])
        total_count = len(results)
        
        return jsonify({
            'status': 'success',
            'message': f'Full analysis completed: {success_count}/{total_count} tickers processed',
            'results': {
                'total': total_count,
                'successful': success_count,
                'failed': total_count - success_count
            }
        })
        
    except Exception as e:
        logger.error(f"Error running full analysis: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

@app.route('/api/config')
def get_config():
    """Get current configuration (without sensitive data)"""
    try:
        return jsonify({
            'status': 'success',
            'config': {
                'base_dir': str(Config.BASE_DIR),
                'output_dir': str(Config.OUTPUT_DIR),
                'default_stocks': Config.DEFAULT_STOCKS,
                'max_retries': Config.MAX_RETRIES,
                'retry_delay': Config.RETRY_DELAY,
                'chunk_size': Config.CHUNK_SIZE
            }
        })
    except Exception as e:
        logger.error(f"Error getting config: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

if __name__ == '__main__':
    # Create output directory if it doesn't exist
    Config.create_directories()
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5001) 