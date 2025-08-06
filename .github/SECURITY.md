# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability in this forked Farcaster MCP project, please follow these steps:

1. **DO NOT** open a public issue
2. Send a detailed report to the maintainer via GitHub Security Advisories
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if available)

## Security Measures

This repository implements comprehensive security scanning:

### Automated Security Checks
- **CodeQL Analysis**: Deep semantic code analysis for Python
- **Dependency Scanning**: Multiple tools check for known vulnerabilities
- **Secret Detection**: TruffleHog and Gitleaks scan for exposed credentials
- **SAST Tools**: Bandit and Semgrep for static analysis
- **Docker Security**: Trivy scans for container vulnerabilities
- **License Compliance**: Automated license checking

### Key Security Considerations

1. **MNEMONIC Environment Variable**: 
   - Never commit mnemonics or private keys
   - Use secure secret management in production
   - Rotate credentials regularly

2. **API Endpoints**:
   - The application connects to `api.warpcast.com`
   - Runs on `127.0.0.1:8080` by default
   - Consider implementing rate limiting

3. **Dependencies**:
   - `httpx`: HTTP client library
   - `farcaster`: Farcaster protocol library
   - `mcp[cli]`: Model Context Protocol
   - All dependencies are scanned for vulnerabilities

## Best Practices

- Review all security scan results before deployment
- Keep dependencies updated
- Use environment variables for sensitive configuration
- Implement proper input validation
- Follow the principle of least privilege
- Enable GitHub Security features (Dependabot, Secret scanning)

## Security Scan Schedule

- **On every push** to main/develop branches
- **On every pull request** to main branch
- **Weekly scheduled scans** (Mondays at 1:30 AM UTC)

## Contact

For security concerns, please use GitHub Security Advisories or contact the repository maintainer directly.