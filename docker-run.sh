#!/bin/bash
# Build and run the LlamaCalc Docker container

set -e

# Print header
echo "=========================================="
echo "LlamaCalc Docker Helper"
echo "=========================================="

# Build the Docker image
echo "Building Docker image..."
docker build -t llamacalc:latest .

# Function to display usage
show_usage() {
  echo "Usage: ./docker-run.sh [OPTION]"
  echo ""
  echo "Options:"
  echo "  -i, --interactive  Run in interactive mode"
  echo "  -b, --batch FILE   Run in batch mode with specified JSON file"
  echo "  -h, --help         Show this help message"
  echo ""
  echo "Examples:"
  echo "  ./docker-run.sh -i                     # Run in interactive mode"
  echo "  ./docker-run.sh -b ./data/batch.json   # Process batch file"
  echo ""
}

# Process command line arguments
if [ $# -eq 0 ]; then
  show_usage
  exit 0
fi

case "$1" in
  -i|--interactive)
    echo "Running in interactive mode..."
    docker run -it --rm --name llamacalc-interactive \
      -v "$PWD/cache:/home/llamauser/.llamacalc" \
      llamacalc:latest --interactive
    ;;
  -b|--batch)
    if [ -z "$2" ]; then
      echo "Error: Batch file path not specified."
      show_usage
      exit 1
    fi
    
    BATCH_FILE=$(realpath "$2")
    if [ ! -f "$BATCH_FILE" ]; then
      echo "Error: Batch file not found at $BATCH_FILE"
      exit 1
    fi
    
    echo "Running batch processing with file: $BATCH_FILE"
    docker run -it --rm --name llamacalc-batch \
      -v "$PWD/cache:/home/llamauser/.llamacalc" \
      -v "$(dirname "$BATCH_FILE"):/data" \
      llamacalc:latest --batch-file "/data/$(basename "$BATCH_FILE")" --json
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

echo "Done!" 