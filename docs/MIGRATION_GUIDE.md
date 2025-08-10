# Migration Guide: Old EquityExplorer to New Structure

This guide helps you transition from the old EquityExplorer codebase to the new, improved structure.

## 🚨 Breaking Changes

The new structure introduces several breaking changes:

1. **File Structure**: Completely reorganized into modular components
2. **Configuration**: Moved from hardcoded values to configuration files
3. **Dependencies**: New requirements and import structure
4. **Execution**: New CLI interface instead of running Python files directly

## 📁 File Mapping

| Old File | New File | Purpose |
|----------|----------|---------|
| `---Main.py` | `equity_explorer.py` | Main orchestrator |
| `Variables.py` | `config.py` | Configuration management |
| `StocksConverter.py` | `csv_processor.py` | CSV processing |
| `TodayDateConverter.py` | `csv_processor.py` | CSV processing |
| `---Date and Stocks.py` | `equity_explorer.py` | Main orchestrator |

## 🔄 Migration Steps

### Step 1: Backup Your Current Setup

```bash
# Create a backup of your current working setup
cp -r . ../EquityExplorer_backup
```

### Step 2: Install New Dependencies

```bash
# Install the new requirements
pip install -r requirements.txt
```

### Step 3: Configure the New System

```bash
# Copy the example configuration
cp config.example.py config.py

# Edit the configuration file
nano config.py
```

**Required Configuration:**
```python
# API Configuration
FINANCIAL_MODELING_PREP_API_KEY = 'your_actual_api_key'

# Anaplan Configuration
ANAPLAN_USER = 'your_username'
ANAPLAN_WORKSPACE_ID = 'your_workspace_id'
ANAPLAN_MODEL_ID = 'your_model_id'
```

### Step 4: Test the New Setup

```bash
# Run the test script
python test_setup.py
```

### Step 5: Update Your Workflow

#### Old Way:
```bash
# Edit Variables.py with paths
# Edit ---Main.py with API keys
# Run ---Main.py
python ---Main.py
```

#### New Way:
```bash
# Process a single ticker
python cli.py ticker AAPL

# Process multiple tickers
python cli.py tickers AAPL MSFT GOOGL

# Run full analysis
python cli.py full
```

## 🔧 Configuration Migration

### Old Variables.py → New config.py

| Old Variable | New Config | Notes |
|--------------|------------|-------|
| `bat1` | `BATCH_SCRIPTS['balance_sheet']` | Automatically managed |
| `bat2` | `BATCH_SCRIPTS['income_statement']` | Automatically managed |
| `bat3` | `BATCH_SCRIPTS['cash_flow']` | Automatically managed |
| `bat4` | `BATCH_SCRIPTS['stocks']` | Automatically managed |
| `bat5` | `BATCH_SCRIPTS['date']` | Automatically managed |

### Old Hardcoded Values → New Configuration

| Old Location | New Location | Description |
|--------------|--------------|-------------|
| `---Main.py` line 15 | `config.py` | API key |
| `---Main.py` line 16 | `config.py` | API key |
| `---Main.py` line 17 | `config.py` | API key |
| Stock list in `---Main.py` | `config.py` | `DEFAULT_STOCKS` |

## 📊 Usage Examples

### Single Ticker Processing

**Old Way:**
```python
# Edit ---Main.py to change ticker
Stocks = ['AAPL']  # Change this line
# Run the file
python ---Main.py
```

**New Way:**
```bash
python cli.py ticker AAPL
```

### Multiple Ticker Processing

**Old Way:**
```python
# Edit ---Main.py to change ticker list
Stocks = ['AAPL', 'MSFT', 'GOOGL']  # Change this line
# Run the file
python ---Main.py
```

**New Way:**
```bash
python cli.py tickers AAPL MSFT GOOGL
```

### Custom Stock Lists

**Old Way:**
```python
# Edit the Stocks list in ---Main.py
Stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
```

**New Way:**
```python
# Edit config.py
DEFAULT_STOCKS = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
```

## 🆘 Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   # Make sure you're in the right directory
   cd EquityExplorer
   
   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Configuration Errors**
   ```bash
   # Check your config.py file
   python test_setup.py
   ```

3. **API Key Issues**
   - Verify your API key in `config.py`
   - Check if the API key is valid
   - Ensure you have sufficient API credits

4. **Anaplan Integration Issues**
   - Verify your Anaplan credentials
   - Check if batch scripts exist and are properly configured
   - Ensure Anaplan service is accessible

### Getting Help

1. Check the logs in `equity_explorer.log`
2. Run `python test_setup.py` to verify setup
3. Review the new README.md for detailed usage instructions
4. Check that all batch scripts are in the correct location

## ✅ Migration Checklist

- [ ] Backup current working setup
- [ ] Install new dependencies (`pip install -r requirements.txt`)
- [ ] Copy `config.example.py` to `config.py`
- [ ] Configure API keys and Anaplan credentials in `config.py`
- [ ] Run `python test_setup.py` to verify setup
- [ ] Test with a single ticker: `python cli.py ticker AAPL`
- [ ] Verify output files are generated correctly
- [ ] Test Anaplan integration
- [ ] Update any automation scripts to use new CLI

## 🎯 Benefits of the New Structure

1. **Maintainability**: Modular, well-organized code
2. **Cross-Platform**: Works on Windows, macOS, and Linux
3. **Security**: No hardcoded API keys or credentials
4. **Reliability**: Better error handling and retry logic
5. **Flexibility**: Easy to customize and extend
6. **Monitoring**: Comprehensive logging and debugging
7. **Automation**: CLI interface for scripting and automation

## 🔮 Next Steps

After successful migration:

1. **Customize**: Modify `config.py` for your specific needs
2. **Automate**: Use the CLI in scripts and cron jobs
3. **Extend**: Add new features using the modular architecture
4. **Monitor**: Use the logging system for monitoring and debugging

---

**Need Help?** Run `python test_setup.py` to diagnose any issues with your setup. 