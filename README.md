# EquityExplorer 📊

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://github.com/yourusername/EquityExplorer)

A modern, clean, and maintainable financial data analysis tool that integrates with Anaplan to provide comprehensive stock market analysis.

## 🚀 Features

- **Automated Financial Data Collection**: Fetches Income Statements, Cash Flow Statements, and Balance Sheets from Financial Modeling Prep API
- **Intelligent Data Processing**: Automatically cleans and formats CSV data for optimal analysis
- **Anaplan Integration**: Seamless upload to Anaplan business planning platform
- **Cross-Platform Support**: Works on Windows, macOS, and Linux
- **Robust Error Handling**: Comprehensive retry logic and logging
- **Flexible Configuration**: Environment-based configuration management
- **Command Line Interface**: Easy-to-use CLI for automation and scripting

## 📋 Requirements

- Python 3.7+
- Anaplan access with upload permissions
- Financial Modeling Prep API key
- Internet connection for API calls

## 🛠️ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/EquityExplorer.git
cd EquityExplorer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure the Application
```bash
# Copy the example configuration
cp config.example.py config.py

# Edit config.py with your credentials
nano config.py  # or use your preferred editor
```

### 4. Set Environment Variables (Recommended)
```bash
export FMP_API_KEY="your_api_key_here"
export ANAPLAN_USER="your_username"
export ANAPLAN_WORKSPACE_ID="your_workspace_id"
export ANAPLAN_MODEL_ID="your_model_id"
```

## ⚙️ Configuration

Edit `config.py` with your credentials:

```python
# API Configuration
FINANCIAL_MODELING_PREP_API_KEY = 'your_api_key_here'

# Anaplan Configuration
ANAPLAN_USER = 'your_username'
ANAPLAN_WORKSPACE_ID = 'your_workspace_id'
ANAPLAN_MODEL_ID = 'your_model_id'

# Customize stock list
DEFAULT_STOCKS = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
```

## 🚀 Usage

### Interactive Mode (Recommended for new users)
```bash
python main.py
```

### Command Line Interface

```bash
# Process a single ticker
python cli.py ticker AAPL

# Process multiple tickers
python cli.py tickers AAPL MSFT GOOGL

# Run full analysis with default stocks
python cli.py full

# Enable verbose logging
python cli.py --verbose ticker AAPL
```

### Programmatic Usage

```python
from src.equity_explorer import EquityExplorer

# Initialize the explorer
explorer = EquityExplorer()

# Process a single ticker
results = explorer.run_single_ticker_analysis('AAPL')

# Process multiple tickers
results = explorer.process_multiple_tickers(['AAPL', 'MSFT', 'GOOGL'])

# Run full analysis
results = explorer.run_full_analysis()
```

## 📁 Project Structure

```
EquityExplorer/
├── src/                    # Core Python source code
│   ├── __init__.py
│   ├── equity_explorer.py
│   ├── financial_data_fetcher.py
│   ├── csv_processor.py
│   └── batch_script_manager.py
├── frontend/               # Web interface
├── scripts/                # Utility scripts and batch files
├── data/                   # Data files
├── tests/                  # Test files
├── docs/                   # Documentation
├── main.py                 # Main application entry point
├── cli.py                  # Command line interface
├── config.py               # Configuration file (create from config.example.py)
└── requirements.txt        # Python dependencies
```

For detailed structure information, see [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md).

## 🔧 How It Works

1. **Data Fetching**: Retrieves financial statements from Financial Modeling Prep API
2. **Data Processing**: Cleans and formats CSV data for analysis
3. **File Management**: Organizes output files in structured directories
4. **Anaplan Integration**: Uploads processed data using batch scripts
5. **Logging & Monitoring**: Comprehensive logging for debugging and monitoring

## 📊 Supported Financial Statements

- **Income Statement**: Revenue, expenses, and profit/loss data
- **Cash Flow Statement**: Operating, investing, and financing cash flows
- **Balance Sheet**: Assets, liabilities, and shareholder equity

## 🛡️ Security Features

- Environment variable configuration
- No hardcoded API keys
- Secure credential management
- Input validation and sanitization

## 📝 Logging

The application provides comprehensive logging:

- **File Logging**: All operations logged to `equity_explorer.log`
- **Console Output**: Real-time status updates
- **Error Tracking**: Detailed error information for debugging
- **Performance Metrics**: Processing time and success rates

## 🔄 Error Handling

- **Automatic Retries**: Configurable retry logic for API failures
- **Graceful Degradation**: Continues processing other tickers if one fails
- **Detailed Error Messages**: Clear error reporting for troubleshooting
- **Recovery Mechanisms**: Automatic cleanup and recovery from failures

## 🚀 Performance Optimizations

- **Batch Processing**: Efficient handling of multiple tickers
- **Rate Limiting**: Respectful API usage with configurable delays
- **Memory Management**: Efficient file handling and processing
- **Parallel Execution**: Concurrent batch script execution where possible

## 🧪 Testing

Run the test suite to ensure everything is working correctly:

```bash
python -m pytest tests/
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/EquityExplorer.git
cd EquityExplorer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install pytest black flake8

# Run tests
pytest

# Format code
black src/ tests/

# Lint code
flake8 src/ tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:

1. Check the logs in `equity_explorer.log`
2. Review the configuration in `config.py`
3. Ensure all dependencies are installed
4. Verify your API credentials and Anaplan access
5. [Open an issue](https://github.com/yourusername/EquityExplorer/issues) on GitHub

## 🔮 Future Enhancements

- [ ] Web-based dashboard
- [ ] Real-time data streaming
- [ ] Advanced analytics and visualization
- [ ] Machine learning insights
- [ ] Multi-exchange support
- [ ] Historical data analysis
- [ ] Portfolio optimization tools

## 📚 API Documentation

- **Financial Modeling Prep**: [API Documentation](https://financialmodelingprep.com/developer/docs/)
- **Anaplan**: [API Documentation](https://help.anaplan.com/)

## 🙏 Acknowledgments

- Financial Modeling Prep for providing financial data APIs
- Anaplan for business planning platform integration
- The open-source community for various Python libraries

---

**Note**: This is a refactored and improved version of the original EquityExplorer. The new version provides better maintainability, cross-platform support, and enhanced error handling while preserving all original functionality.

⭐ **Star this repository if you find it helpful!** 
