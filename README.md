# Anthem PPO URL Extractor

## Project Overview
This repository contains a Python script designed for efficient extraction of machine-readable file URLs corresponding to Anthem's Preferred Provider Organization (PPO) health plans in New York State. The script handles extremely large JSON files by leveraging the `ijson` library for streaming parsing to minimize memory usage and improve performance.

## Installation and Setup

### Prerequisites
- Python 3.x
- `ijson` library

### Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/asharm0662/serif_json-url-extractor.git
   ```
2. **Install the required Python package:**
   ```bash
   cd <location to repo>
   pip install -r requirements.txt
   ```
3. **Usage**
   ```bash
   python extract_urls.py <input_file_path> <output_file_path>
   ```
   ```bash
   python extract_urls.py large_input.json output_urls.csv
   ```

## Solution Description
The script parses a large JSON file to find URLs that match specific criteria—entries describing Anthem's PPO plans located in New York. The output is a list of URLs saved to a specified text file.

## Script Details
- **Input Handling:** The script uses `argparse` to take input and output file paths from the command line, allowing flexibility in file management.
- **JSON Parsing:** Utilizes `ijson` for incremental parsing of JSON data, enabling the script to handle large files without loading the entire file into memory.
- **Data Processing:** Iterates through nested JSON structures to extract URLs based on matching criteria within descriptions.

## Performance and Trade-offs
### Time Metrics
- **Development Time:** Approximately 90 minutes.
- **Execution Time:** About 3 minutes for parsing and writing URLs from the large JSON file.

### Memory and Computational Trade-offs
- **Memory Efficiency:** By using `ijson` for streaming parsing, the script maintains low memory usage, crucial for processing files that exceed memory capacities of most standard systems. This approach avoids memory overflow and crashing issues commonly associated with loading large files in memory.
- **Computational Speed:** While `ijson` reduces memory load, it processes the file more slowly than loading the entire JSON into memory (e.g., with standard `json.load`). This trade-off is critical for the feasibility of processing very large datasets on limited-resource systems.
- **Scalability:** The script is designed to scale with file size, maintaining performance across varying file sizes without additional memory requirement adjustments.

### Limitations and Considerations
- **Data Complexity:** The script assumes a specific JSON structure and may require adjustments if the data format varies.
- **Error Handling:** Limited error handling for unexpected data formats or read/write errors, which could be expanded in future versions for robustness.

