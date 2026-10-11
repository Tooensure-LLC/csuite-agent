# Queue

Envelope protocol: `pmcro.message/v1`. Delivery: at-least-once. Deduplication: `messageId + dedupeDigest`; `contentDigest` protects the exact immutable envelope. Claiming uses leases; expired leases recover; retries are bounded; exhausted messages dead-letter. ACK writes an immutable receipt. Queue transport state is separate from the immutable envelope.
