# Alert Manager body checker

AlertManager sends alerts to the receivers, and each alert is assigned a unique identifier known as the `fingerprint`. This fingerprint is computed as a hash of the label set of the alert.

The purpose of this repository is to examine the behavior of the fingerprint in various scenarios.
