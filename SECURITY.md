# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of EquityExplorer seriously. If you believe you have found a security vulnerability, please report it to us as described below.

**Please do not report security vulnerabilities through public GitHub issues.**

### How to Report a Security Vulnerability

1. **Email Security Team**: Send an email to [security@equityexplorer.com](mailto:security@equityexplorer.com)
   - Use a descriptive subject line
   - Include detailed information about the vulnerability
   - Provide steps to reproduce the issue

2. **Alternative Contact**: If you cannot reach us via email, please contact the maintainers directly through GitHub.

### What to Include in Your Report

To help us better understand and address the vulnerability, please include:

- **Description**: A clear description of the vulnerability
- **Impact**: The potential impact if exploited
- **Steps to Reproduce**: Detailed steps to reproduce the issue
- **Environment**: Your operating system, Python version, and EquityExplorer version
- **Proof of Concept**: If possible, include a proof of concept
- **Timeline**: Any deadlines or time constraints
- **Contact Information**: How we can reach you for additional information

### What Happens Next

1. **Acknowledgment**: You will receive an acknowledgment within 48 hours
2. **Investigation**: Our security team will investigate the report
3. **Updates**: We will keep you informed of our progress
4. **Resolution**: Once resolved, we will coordinate disclosure with you
5. **Credit**: We will credit you in our security advisories (unless you prefer to remain anonymous)

### Disclosure Timeline

- **Critical vulnerabilities**: Fixed and disclosed within 7 days
- **High severity vulnerabilities**: Fixed and disclosed within 14 days
- **Medium severity vulnerabilities**: Fixed and disclosed within 30 days
- **Low severity vulnerabilities**: Fixed and disclosed within 90 days

## Security Best Practices

### For Users

1. **Keep Updated**: Always use the latest stable version of EquityExplorer
2. **Secure Configuration**: Use environment variables for sensitive configuration
3. **Network Security**: Use HTTPS for all API communications
4. **Access Control**: Limit access to your Anaplan workspace and API keys
5. **Monitor Logs**: Regularly review application logs for suspicious activity

### For Developers

1. **Dependency Updates**: Keep dependencies updated and monitor for security advisories
2. **Input Validation**: Always validate and sanitize user input
3. **Authentication**: Implement proper authentication and authorization
4. **Secrets Management**: Never commit API keys or credentials to version control
5. **Code Review**: Conduct security-focused code reviews

## Security Features

EquityExplorer includes several security features:

- **Environment Variable Configuration**: No hardcoded credentials
- **Input Validation**: Comprehensive input sanitization
- **Secure Communication**: HTTPS for all external API calls
- **Error Handling**: Secure error messages that don't leak sensitive information
- **Logging**: Secure logging without sensitive data exposure

## Security Updates

Security updates are released as patch versions (e.g., 1.0.1, 1.0.2) and should be applied as soon as possible.

### Updating Security Patches

```bash
# Update to latest version
pip install --upgrade equity-explorer

# Or update from source
git pull origin main
pip install -r requirements.txt
```

## Responsible Disclosure

We believe in responsible disclosure and will work with security researchers to:

- Validate reported vulnerabilities
- Develop and test fixes
- Coordinate disclosure timelines
- Credit researchers appropriately

## Security Contacts

- **Security Team**: [security@equityexplorer.com](mailto:security@equityexplorer.com)
- **Maintainers**: [@maintainers](https://github.com/orgs/equityexplorer/teams/maintainers)
- **Emergency**: For critical issues requiring immediate attention

## Security Hall of Fame

We recognize security researchers who help improve EquityExplorer's security:

- [Your Name] - Reported [vulnerability description] (Date)
- [Add more as vulnerabilities are reported and fixed]

---

Thank you for helping keep EquityExplorer secure! 🔒 