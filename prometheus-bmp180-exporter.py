#!/usr/bin/python

import argparse

from wsgiref.simple_server import make_server

from prometheus_client import make_wsgi_app, Metric, REGISTRY

from Adafruit.Adafruit_BMP085 import BMP085


PORT = 9091


class BMP180Collector():

    def collect(self):
        bmp = BMP085(0x77)
        temp = bmp.readTemperature()
        pressure = bmp.readPressure()

        temp_metric = Metric('bmp180_temp', 'BMP180 temperature', 'gauge')
        yield temp_metric

        pressure_metric = Metric('bmp180_pressure', 'BMP180 pressure', 'gauge')
        yield pressure_metric


def main():
      parser = argparse.ArgumentParser(description='BMP180 exporter for Prometheus')
      parser.add_argument('-p', '--port', help=f'exporter exposed port (default {PORT})', type=int, default=PORT)
      args = parser.parse_args()

      REGISTRY.register(BMP180Collector())

      app = make_wsgi_app()
      httpd = make_server('', args.port, app)
      httpd.serve_forever()


if __name__ == "__main__":
    main()
