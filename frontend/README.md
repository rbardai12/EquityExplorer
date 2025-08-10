# EquityExplorer Frontend

A modern, responsive web interface for the EquityExplorer financial analysis tool. This frontend provides an intuitive way to interact with the EquityExplorer backend, process ticker symbols, view generated data, and manage files.

## Features

- **Modern Dashboard**: Clean, responsive interface built with Bootstrap 5
- **Real-time Processing**: Process single or multiple ticker symbols
- **File Management**: View, download, and delete generated CSV files
- **Data Visualization**: Interactive tables with DataTables integration
- **System Monitoring**: Real-time status updates and metrics
- **Configuration Display**: View current system configuration
- **Progress Tracking**: Visual feedback during processing operations

## Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation

1. **Install Dependencies**
   ```bash
   pip install -r ../requirements.txt
   ```

2. **Start the Frontend**

   **Windows:**
   ```cmd
   start_frontend.bat
   ```

   **macOS/Linux:**
   ```bash
   chmod +x start_frontend.sh
   ./start_frontend.sh
   ```

   **Manual Start:**
   ```bash
   cd frontend
   python start_frontend.py
   ```

3. **Open Your Browser**
   Navigate to: `http://localhost:5000`

## Usage

### Dashboard Overview

The dashboard displays key metrics and system status:
- **Total Files**: Number of generated CSV files
- **Tickers Available**: Number of configured stock symbols
- **Last Processed**: Date of most recent processing
- **System Status**: Current system operational status

### Processing Tickers

#### Single Ticker
1. Enter a ticker symbol (e.g., AAPL, MSFT)
2. Click "Process" button
3. Monitor progress and view results

#### Multiple Tickers
1. Enter comma-separated ticker symbols (e.g., AAPL,MSFT,GOOGL)
2. Click "Process All" button
3. Track progress across all tickers

#### Full Analysis
1. Click "Run Full Analysis" button
2. Confirm the operation
3. Monitor progress for all configured tickers

### File Management

#### Viewing Files
- Click "View" button on any file to see its contents
- Data is displayed in an interactive table
- First 100 rows are shown by default

#### Downloading Files
- Click the download icon to save CSV files locally
- Files are downloaded with original names

#### Deleting Files
- Click the trash icon to remove files
- Confirmation dialog prevents accidental deletion

### Configuration

The configuration panel displays:
- Output directory path
- Maximum retry attempts
- Retry delay settings
- Chunk size for processing

## API Endpoints

The frontend communicates with the backend through these REST API endpoints:

- `GET /api/status` - System status and metrics
- `GET /api/tickers` - Available ticker symbols
- `POST /api/process-ticker` - Process single ticker
- `POST /api/process-tickers` - Process multiple tickers
- `POST /api/run-full-analysis` - Run complete analysis
- `GET /api/files` - List generated files
- `GET /api/files/<filename>` - View file contents
- `GET /api/download/<filename>` - Download file
- `DELETE /api/delete/<filename>` - Delete file
- `GET /api/config` - System configuration

## Troubleshooting

### Common Issues

1. **Import Errors**
   - Ensure all dependencies are installed: `pip install -r ../requirements.txt`
   - Check that the parent directory is in Python path

2. **Port Already in Use**
   - Change the port in `start_frontend.py` or set `PORT` environment variable
   - Kill existing processes using port 5000

3. **Configuration Errors**
   - Verify `config.py` exists in the parent directory
   - Check that required directories can be created

4. **Frontend Not Loading**
   - Check browser console for JavaScript errors
   - Verify Flask server is running without errors
   - Check network connectivity

### Logs

The application logs important events to the console:
- Startup sequence and dependency checks
- API request processing
- Error conditions and stack traces

## Development

### Project Structure

```
frontend/
├── app.py                 # Flask application
├── start_frontend.py      # Startup script
├── start_frontend.bat     # Windows startup
├── start_frontend.sh      # Unix startup
├── templates/
│   └── index.html        # Main HTML template
└── README.md             # This file
```

### Customization

#### Styling
- Modify CSS variables in `index.html` for theme changes
- Bootstrap 5 classes provide responsive design
- Custom CSS can be added to the `<style>` section

#### Functionality
- Add new API endpoints in `app.py`
- Extend JavaScript functions in the `<script>` section
- Modify HTML structure in the template

#### Configuration
- Environment variables: `PORT`, `HOST`
- Modify `start_frontend.py` for custom startup logic

## Security Notes

- The frontend runs in debug mode by default (development only)
- CORS is enabled for cross-origin requests
- File operations are restricted to the configured output directory
- No authentication is implemented (add as needed for production)

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Performance

- DataTables handles large datasets efficiently
- Lazy loading for file contents
- Auto-refresh every 30 seconds for status updates
- Responsive design for mobile and desktop

## Contributing

1. Follow the existing code style
2. Test changes across different browsers
3. Update documentation for new features
4. Ensure error handling is comprehensive

## License

This frontend is part of the EquityExplorer project and follows the same licensing terms. 