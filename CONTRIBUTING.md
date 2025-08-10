# Contributing to EquityExplorer 🤝

Thank you for your interest in contributing to EquityExplorer! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Git
- A GitHub account

### Development Environment Setup

1. **Fork the repository**
   ```bash
   # Go to https://github.com/yourusername/EquityExplorer
   # Click "Fork" button
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/yourusername/EquityExplorer.git
   cd EquityExplorer
   ```

3. **Set up the upstream remote**
   ```bash
   git remote add upstream https://github.com/original-owner/EquityExplorer.git
   ```

4. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

5. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```

## 🔧 Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/your-bug-description
```

**Branch Naming Convention:**
- `feature/` - New features
- `bugfix/` - Bug fixes
- `hotfix/` - Critical fixes
- `docs/` - Documentation updates
- `test/` - Test improvements

### 2. Make Your Changes

- Write clean, readable code
- Follow the existing code style
- Add comments for complex logic
- Update documentation if needed

### 3. Test Your Changes

```bash
# Run the test suite
pytest

# Run with coverage
pytest --cov=src

# Run specific tests
pytest tests/test_equity_explorer.py
```

### 4. Code Quality Checks

```bash
# Format code with Black
black src/ tests/

# Lint with flake8
flake8 src/ tests/

# Type checking (if using type hints)
mypy src/
```

### 5. Commit Your Changes

```bash
git add .
git commit -m "feat: add new financial data processor

- Implemented new data processing algorithm
- Added unit tests for edge cases
- Updated documentation
- Closes #123"
```

**Commit Message Format:**
```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation
- `style` - Code style changes
- `refactor` - Code refactoring
- `test` - Test additions/changes
- `chore` - Maintenance tasks

### 6. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then go to GitHub and create a Pull Request.

## 📋 Pull Request Guidelines

### Before Submitting

- [ ] Code follows the project's style guidelines
- [ ] All tests pass
- [ ] New tests added for new functionality
- [ ] Documentation updated
- [ ] No sensitive information (API keys, credentials) in code
- [ ] Branch is up to date with main

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Other (please describe)

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes

## Screenshots (if applicable)
Add screenshots for UI changes

## Additional Notes
Any additional information
```

## 🎯 Areas for Contribution

### High Priority
- [ ] Additional financial data sources
- [ ] Performance optimizations
- [ ] Error handling improvements
- [ ] Test coverage expansion

### Medium Priority
- [ ] Documentation improvements
- [ ] Code refactoring
- [ ] New CLI commands
- [ ] Configuration enhancements

### Low Priority
- [ ] UI/UX improvements
- [ ] Additional export formats
- [ ] Plugin system
- [ ] Internationalization

## 🐛 Reporting Issues

### Bug Report Template

```markdown
## Bug Description
Clear description of the bug

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: [e.g., Windows 10, macOS 12.0, Ubuntu 20.04]
- Python Version: [e.g., 3.9.7]
- EquityExplorer Version: [e.g., 1.0.0]

## Additional Information
Any other relevant information
```

### Feature Request Template

```markdown
## Feature Description
Clear description of the feature

## Use Case
Why this feature is needed

## Proposed Solution
How you think it should work

## Alternatives Considered
Other approaches you considered

## Additional Information
Any other relevant information
```

## 📚 Code Style Guidelines

### Python Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Keep functions small and focused
- Add type hints where appropriate
- Use docstrings for public functions

### Example

```python
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)


def process_financial_data(
    ticker: str, 
    data_type: str, 
    start_date: Optional[str] = None
) -> List[dict]:
    """
    Process financial data for a given ticker.
    
    Args:
        ticker: Stock ticker symbol
        data_type: Type of financial data to process
        start_date: Optional start date for data range
        
    Returns:
        List of processed financial data records
        
    Raises:
        ValueError: If ticker is invalid
        ConnectionError: If API connection fails
    """
    if not ticker or not ticker.strip():
        raise ValueError("Ticker cannot be empty")
    
    logger.info(f"Processing {data_type} data for {ticker}")
    
    # Implementation here...
    return []
```

## 🧪 Testing Guidelines

### Test Structure

```python
import pytest
from src.equity_explorer import EquityExplorer


class TestEquityExplorer:
    """Test suite for EquityExplorer class."""
    
    @pytest.fixture
    def explorer(self):
        """Create a test instance of EquityExplorer."""
        return EquityExplorer()
    
    def test_process_single_ticker(self, explorer):
        """Test processing a single ticker."""
        result = explorer.process_single_ticker("AAPL")
        assert result is not None
        assert "ticker" in result
        assert result["ticker"] == "AAPL"
    
    def test_invalid_ticker_raises_error(self, explorer):
        """Test that invalid ticker raises appropriate error."""
        with pytest.raises(ValueError, match="Invalid ticker"):
            explorer.process_single_ticker("")
```

### Test Naming

- Test methods should be descriptive
- Use `test_` prefix
- Group related tests in test classes
- Use fixtures for common setup

## 📖 Documentation Guidelines

### Code Documentation

- Use clear, concise docstrings
- Follow Google or NumPy docstring format
- Document all public functions and classes
- Include examples for complex functions

### README Updates

- Update README.md for new features
- Add usage examples
- Update installation instructions if needed
- Keep project structure current

## 🔒 Security Guidelines

### Never Commit

- API keys
- Passwords
- Database credentials
- Private keys
- Personal information

### Use Environment Variables

```python
import os

api_key = os.getenv('API_KEY')
if not api_key:
    raise ValueError("API_KEY environment variable not set")
```

## 🚀 Release Process

### Version Bumping

- Use semantic versioning (MAJOR.MINOR.PATCH)
- Update version in `__init__.py`
- Update CHANGELOG.md
- Tag releases in Git

### Release Checklist

- [ ] All tests pass
- [ ] Documentation updated
- [ ] Version bumped
- [ ] CHANGELOG updated
- [ ] Release notes written
- [ ] Git tag created

## 🤝 Community Guidelines

### Be Respectful

- Be kind and respectful to all contributors
- Welcome newcomers and help them get started
- Provide constructive feedback
- Respect different opinions and approaches

### Communication

- Use clear, professional language
- Ask questions if something is unclear
- Provide context when reporting issues
- Be patient with responses

## 📞 Getting Help

### Questions and Discussion

- Use GitHub Discussions for general questions
- Open an issue for bugs or feature requests
- Join our community chat (if available)

### Contact Maintainers

- Tag maintainers in issues when appropriate
- Use @mentions for specific questions
- Be specific about what you need help with

## 🙏 Recognition

Contributors will be recognized in:

- README.md contributors section
- Release notes
- Project documentation
- GitHub contributors page

---

Thank you for contributing to EquityExplorer! Your contributions help make this project better for everyone. 🎉 