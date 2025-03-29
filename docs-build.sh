#!/bin/bash
# Script to build and serve the LlamaCalc documentation

set -e

# Print header
echo "=========================================="
echo "LlamaCalc Documentation Builder"
echo "=========================================="

# Function to check if a command exists
command_exists() {
  command -v "$1" >/dev/null 2>&1
}

# Check if Python is installed
if ! command_exists python3; then
  echo "Error: Python 3 is required but not installed."
  exit 1
fi

# Create a virtual environment if it doesn't exist
if [ ! -d "docs_venv" ]; then
  echo "Creating virtual environment for documentation..."
  python3 -m venv docs_venv
fi

# Activate the virtual environment
source docs_venv/bin/activate

# Install dependencies
echo "Installing documentation dependencies..."
pip install --quiet --upgrade pip
pip install --quiet -r requirements-docs.txt

# Function to display usage
show_usage() {
  echo "Usage: ./docs-build.sh [OPTION]"
  echo ""
  echo "Options:"
  echo "  -b, --build     Build the documentation site"
  echo "  -s, --serve     Build and serve the documentation site locally"
  echo "  -h, --help      Show this help message"
  echo ""
}

# Process command line arguments
if [ $# -eq 0 ]; then
  show_usage
  exit 0
fi

case "$1" in
  -b|--build)
    echo "Building documentation..."
    mkdocs build
    echo "Documentation built successfully! Output is in the 'site' directory."
    ;;
  -s|--serve)
    echo "Building and serving documentation..."
    echo "Open http://127.0.0.1:8000 in your web browser to view."
    echo "Press Ctrl+C to stop the server."
    mkdocs serve
    ;;
  -h|--help)
    show_usage
    ;;
  *)
    echo "Error: Unknown option $1"
    show_usage
    exit 1
    ;;
esac

# Deactivate the virtual environment
deactivate

echo "Done!" 