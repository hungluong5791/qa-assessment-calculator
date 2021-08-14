# Sample Gauge + Taiko Automation Project

## Prerequisites
- NodeJS + Yarn
- [Gauge](https://docs.gauge.org/getting_started/installing-gauge.html)

## Build
    
    yarn install

## Configuration
Configuration are passed to the execution using Gauge [Environment](https://docs.gauge.org/configuration.html).

### Environments
To simulate production project, a `BASE_URL` environment variable is defined in each execution environment
- `dev`: the development machine, running the local browser
- `ci`: the CI environment, running a headless browser

### Browsers
- `chrome`: standard profile for Chrome
- `chrome_optimized`: optimized for parallel Chrome instances (see [reference](https://docs.taiko.dev/frequently_asked_questions/#how-can-i-optimize-chrome-instances-for-parallel-runs%3F))
- `firefox`: standard profile for Firefox Nightly

These values can be passed to Gauge to specified the environment/browser to run the test against i.e

    gauge run specs --env dev,chrome

If no browser profile is specified, tests will executed using the embedded Chromium browser managed by Taiko.

## Running the Scenarios

### Site Under Test

    https://www.online-calculator.com


### Specifications

### Execution

    gauge run specs

### Reporting
The generated HTML report can be found under `./reports/html-report/index.html`