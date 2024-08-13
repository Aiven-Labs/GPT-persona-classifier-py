# GPT-persona-classifier-py

This project allows you to classify a dataset of contacts into personas based on their job-title.

## Dependencies

This project runs as a command line tool (CLI) TBD using Python and the [Vertex AI](https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform).

## Usage

Run the command from the command line:

```python
python persona_classifier.py <PATH_TO_CSV_FILE> --personas <PATH_TO_PERSONAS_JSON_FILE> --output_path <FILE_PATH OR SQL_ENDPOINT_URI>
```

The data returned is the same as the input with the additional column `persona` appended to the end.

### Supported output types

- CSV

### Roadmap

- support for SQL endpoints
- support for JSON output
- support for Excel output
- support for plot output
- support for opensearch output
- support for `redis-protocol` output

### Contribution

Contributions are welcome. Please review our [contribution guidelines](CONTRIBUTING.md).
