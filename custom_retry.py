from google.cloud import storage
from google.cloud.storage.retry import DEFAULT_RETRY


def configure_retries(bucket_name, blob_name):
    """Configures retries with customizations."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The ID of your GCS object
    # blob_name = "your-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # Customize retry with a deadline of 500 seconds (default=120 seconds).
    modified_retry = DEFAULT_RETRY.with_deadline(500.0)
    # Customize retry with an initial wait time of 1.5 (default=1.0).
    # Customize retry with a wait time multiplier per iteration of 1.2 (default=2.0).
    # Customize retry with a maximum wait time of 45.0 (default=60.0).
    modified_retry = modified_retry.with_delay(initial=1.5, multiplier=1.2, maximum=45.0)

    # blob.delete() uses DEFAULT_RETRY_IF_GENERATION_SPECIFIED by default.
    # Override with modified_retry so the function retries even if the generation
    # number is not specified.
    print(
        f"The following library method is customized to be retried according to the following configurations: {modified_retry}"
    )

    blob.delete(retry=modified_retry)
    print(f"Blob {blob_name} deleted with a customized retry strategy.")
