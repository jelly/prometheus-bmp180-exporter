# Prometheus BMP180 Exporter

A BMP180 sensor exporter which exports the temperature (in celcius) and
humidity from a BMP180 sensor. Suitable for a RaspberryPi connected i2c.

# Dependencies

* python
* prometheus_client
* python-smbus

# Usage

Run the exporter

  python prometheus-bmp180-exporter.py

The default port is 9091, visit metrics [http://localhost:9091/ http://localhost:9091].
