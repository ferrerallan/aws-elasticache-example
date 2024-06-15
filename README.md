
# AWS ElastiCache Example

## Description

This project provides an example of how to use AWS ElastiCache with Python. It includes scripts to read from and write to an ElastiCache instance, demonstrating basic usage and integration with Python applications.

## Requirements

- Python 3.6 or higher
- AWS account with ElastiCache setup
- `boto3` library

## Mode of Use

1. Clone the repository:
   ```bash
   git clone https://github.com/ferrerallan/aws-elasticache-example.git
   ```
2. Navigate to the project directory:
   ```bash
   cd aws-elasticache-example
   ```
3. Install the dependencies:
   ```bash
   pip install boto3
   ```
4. Configure your AWS credentials:
   ```bash
   aws configure
   ```
5. Run the write script to add data to ElastiCache:
   ```bash
   python write.py
   ```
6. Run the read script to retrieve data from ElastiCache:
   ```bash
   python read.py
   ```

## Files

- `write.py`: Script to write data to ElastiCache.
- `read.py`: Script to read data from ElastiCache.

## License

This project is licensed under the MIT License.
