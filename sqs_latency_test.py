#!/usr/bin/env python3

import time
import click
import boto3


@click.command()
@click.option("--queue-url", required=True, help="URL of the SQS queue")
@click.option("--message-body", default="Hello, SQS!", help="Body of the message")
@click.option(
    "--interval-seconds", default=1, help="Interval between sending messages in seconds"
)
def send_messages(queue_url, message_body, interval_seconds):
    # Create SQS client
    sqs = boto3.client("sqs")

    # Send messages continuously
    while True:
        start_time = time.time()

        # Send message
        response = sqs.send_message(QueueUrl=queue_url, MessageBody=message_body)

        end_time = time.time()

        # Calculate latency
        latency = end_time - start_time

        # Display output
        print(f"Sent message with latency: {latency:.6f} seconds")

        # Wait for the specified interval
        time.sleep(interval_seconds)


if __name__ == "__main__":
    send_messages()
