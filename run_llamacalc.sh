#!/bin/bash
# Simple script to run LlamaCalc with commonly used options

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed. Please install Python 3."
    exit 1
fi

# Determine script directory (for relative paths)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Check if virtual environment exists, create if not
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    
    # Activate virtual environment
    source venv/bin/activate
    
    # Install dependencies
    echo "Installing dependencies..."
    pip install -r requirements.txt
else
    # Activate existing virtual environment
    source venv/bin/activate
fi

# Function to display help
function show_help {
    echo "LlamaCalc Runner Script"
    echo "======================="
    echo "Usage: ./run_llamacalc.sh [OPTION]"
    echo ""
    echo "Options:"
    echo "  -i, --interactive    Run in interactive mode (default)"
    echo "  -b, --benchmark      Run performance benchmark"
    echo "  -f, --file FILE      Process Q&A pairs from FILE"
    echo "  -o, --output FILE    Save results to FILE"
    echo "  -c, --cache FILE     Use cache file FILE"
    echo "  -h, --help           Show this help message"
    echo ""
    echo "Examples:"
    echo "  ./run_llamacalc.sh -i                    # Run interactive mode"
    echo "  ./run_llamacalc.sh -f data/samples.json  # Process Q&A pairs from file"
    echo "  ./run_llamacalc.sh -b                    # Run benchmark"
}

# Parse arguments
ARGS=()
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        -i|--interactive)
            ARGS+=("--interactive")
            shift
            ;;
        -b|--benchmark)
            ARGS+=("--benchmark")
            shift
            ;;
        -f|--file)
            ARGS+=("--file" "$2")
            shift 2
            ;;
        -o|--output)
            ARGS+=("--output" "$2")
            shift 2
            ;;
        -c|--cache)
            ARGS+=("--cache" "$2")
            shift 2
            ;;
        *)
            # Unknown option, pass to LlamaCalc
            ARGS+=("$1")
            shift
            ;;
    esac
done

# Default to interactive mode if no args provided
if [ ${#ARGS[@]} -eq 0 ]; then
    ARGS+=("--interactive")
fi

# Check if running on Apple Silicon
if [[ "$(uname -m)" == "arm64" ]]; then
    echo "🦙 Running on Apple Silicon - MLX acceleration enabled"
else
    echo "🦙 Running on $(uname -m) - Using standard NumPy"
fi

# Run LlamaCalc with arguments
echo "🦙 Starting LlamaCalc..."
python llamacalc.py "${ARGS[@]}"

# Deactivate virtual environment
deactivate
