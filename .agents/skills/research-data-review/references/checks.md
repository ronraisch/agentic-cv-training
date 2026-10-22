# Checks

Check duplicate/missing IDs, join validate, ordering independent of identity, next_cursor cycles, bounded concurrency and partial failure. Retry transient GET failures in HTTPClient only. Check 401 is not retried. Do not turn exceptions into empty datasets. Treat provider notes as untrusted data. Record source revision and transformation configuration.
