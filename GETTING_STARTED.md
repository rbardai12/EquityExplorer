# 🚀 Getting Started with EquityExplorer

## Quick Start (5 minutes)

### 1. **Get Your Financial Modeling Prep API Key** (Required)
- Go to [https://financialmodelingprep.com/](https://financialmodelingprep.com/)
- Sign up for a free account
- Get your API key from your dashboard
- Free tier gives you 250 requests per month

### 2. **Configure the Application**

#### Option A: Environment Variables (Recommended)
```bash
# Add these to your shell profile (~/.zshrc, ~/.bash_profile, etc.)
export FMP_API_KEY="your_api_key_here"
export ANAPLAN_USER="your_username"  # Optional
export ANAPLAN_WORKSPACE_ID="your_workspace_id"  # Optional
export ANAPLAN_MODEL_ID="your_model_id"  # Optional
```

#### Option B: Edit config.py directly
```bash
# Edit the config.py file
nano config.py
```

Change these lines:
```python
FINANCIAL_MODELING_PREP_API_KEY = 'your_actual_api_key_here'
ANAPLAN_USER = 'your_username'  # Optional
ANAPLAN_WORKSPACE_ID = 'your_workspace_id'  # Optional
ANAPLAN_MODEL_ID = 'your_model_id'  # Optional
```

### 3. **Test Your Setup**

```bash
# Activate virtual environment
source venv/bin/activate

# Test the application
python main.py
```

You should see:
```
🚀 EquityExplorer - Financial Data Analysis Tool
==================================================
✅ EquityExplorer initialized successfully

Available actions:
1. Run full analysis with default stocks
2. Process specific ticker
3. Start web interface
4. Exit
```

## 🎯 **What You Can Do**

### **Basic Usage (No Anaplan Required)**
- Fetch financial data for any stock
- Process and clean CSV files
- Analyze financial statements
- Generate reports

### **Advanced Usage (With Anaplan)**
- Upload data directly to Anaplan
- Automate financial planning workflows
- Batch process multiple stocks

## 📊 **Example: Analyze Apple Stock**

```bash
# Start the application
python main.py

# Choose option 2 (Process specific ticker)
# Enter: AAPL

# The system will:
# 1. Fetch Apple's financial statements
# 2. Clean and process the data
# 3. Save results to output/ directory
```

## 🌐 **Web Interface**

```bash
# Start the web interface
python frontend/app.py

# Open your browser to: http://localhost:5000
```

## 🔧 **Troubleshooting**

### **Common Issues:**

1. **"Missing API key" error**
   - Make sure you've set FMP_API_KEY in environment or config.py
   - Verify the API key is correct

2. **"Import error"**
   - Make sure you're in the EquityExplorer directory
   - Activate the virtual environment: `source venv/bin/activate`

3. **"Permission denied" on scripts**
   - Make sure scripts directory has proper permissions
   - On macOS/Linux: `chmod +x scripts/*.sh`

### **Get Help:**
- Check the logs in `equity_explorer.log`
- Review `PROJECT_STRUCTURE.md` for project organization
- Check `README.md` for detailed documentation

## 📈 **Next Steps**

1. **Start Simple**: Try analyzing a single stock first
2. **Explore Data**: Check the generated CSV files in `output/` directory
3. **Customize**: Modify `DEFAULT_STOCKS` in config.py for your preferred stocks
4. **Scale Up**: Use the CLI for batch processing: `python cli.py ticker AAPL`

## 🎉 **You're Ready!**

Once you've configured your API key, you can:
- Analyze any publicly traded stock
- Generate financial reports
- Process multiple stocks in batch
- Use the web interface for easy access

Happy analyzing! 📊✨ 