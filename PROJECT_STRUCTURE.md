# Project Structure

## Overview
EquityExplorer has been reorganized for better maintainability and clarity. Here's the new structure:

## Directory Layout

```
EquityExplorer/
├── src/                          # Core Python source code
│   ├── __init__.py              # Package initialization
│   ├── equity_explorer.py       # Main EquityExplorer class
│   ├── financial_data_fetcher.py # Financial data fetching logic
│   ├── csv_processor.py         # CSV processing utilities
│   └── batch_script_manager.py  # Batch processing management
│
├── frontend/                     # Web interface
│   ├── app.py                   # Flask web application
│   ├── templates/               # HTML templates
│   ├── start_frontend.py        # Frontend startup script
│   └── README.md                # Frontend documentation
│
├── scripts/                      # Utility scripts and batch files
│   ├── *.bat                    # Windows batch scripts
│   ├── *.sh                     # Unix shell scripts
│   ├── *Converter.py            # Data conversion utilities
│   ├── *Variables.py            # Variable management
│   └── anaplan-connect-*.jar    # Anaplan integration JAR
│
├── data/                         # Data files
│   ├── *.csv                    # CSV data files
│   └── *.xlsx                   # Excel data files
│
├── tests/                        # Test files
│   ├── test_*.py                # Unit and integration tests
│   └── test_setup.py            # Test configuration
│
├── docs/                         # Documentation
│   └── MIGRATION_GUIDE.md       # Migration instructions
│
├── output/                       # Generated output files
├── venv/                         # Python virtual environment
├── main.py                       # Main application entry point
├── cli.py                        # Command line interface
├── config.py                     # Configuration file
├── config.example.py             # Example configuration
├── requirements.txt              # Python dependencies
├── setup.py                      # Package installation script
├── PROJECT_STRUCTURE.md          # This file
└── README.md                     # Main project documentation
```

## Key Changes Made

### 1. **Source Code Organization** (`src/`)
- All core Python modules moved to `src/` directory
- Proper Python package structure with `__init__.py`
- Cleaner import paths and module organization

### 2. **Scripts Consolidation** (`scripts/`)
- All batch files (`.bat`, `.sh`) moved to `scripts/`
- Utility Python scripts for data conversion
- Anaplan integration JAR file

### 3. **Data Management** (`data/`)
- CSV and Excel files organized in `data/` directory
- Cleaner root directory structure
- Better separation of data from code

### 4. **Testing** (`tests/`)
- All test files moved to dedicated `tests/` directory
- Better test organization and discovery

### 5. **Documentation** (`docs/`)
- Migration guides and technical documentation
- Separated from main README for clarity

### 6. **Entry Points**
- `main.py` - Interactive main application
- `cli.py` - Command line interface
- `frontend/app.py` - Web interface

## Usage

### Running the Application
```bash
# Interactive mode
python main.py

# Command line interface
python cli.py ticker AAPL

# Web interface
python frontend/app.py
```

### Development
```bash
# Install in development mode
pip install -e .

# Run tests
python -m pytest tests/

# Clean and rebuild
rm -rf __pycache__/ src/__pycache__/ frontend/__pycache__/
```

## Benefits of New Structure

1. **Cleaner Root Directory**: Only essential files at the top level
2. **Better Organization**: Logical grouping of related files
3. **Easier Maintenance**: Clear separation of concerns
4. **Professional Structure**: Follows Python packaging best practices
5. **Easier Testing**: Dedicated test directory structure
6. **Better Documentation**: Organized documentation structure

## Migration Notes

- Import paths have been updated to use `src.` prefix
- Batch scripts are now in `scripts/` directory
- Data files are in `data/` directory
- Test files are in `tests/` directory
- All functionality remains the same, just better organized 