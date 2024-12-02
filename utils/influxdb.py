from influxdb_client import InfluxDBClient, Point
from django.conf import settings

class InfluxDBHandler:
    def __init__(self):
        self.client = InfluxDBClient(
            url=settings.INFLUXDB['url'],
            token=settings.INFLUXDB['token'],
            org=settings.INFLUXDB['org']
        )
        self.bucket = settings.INFLUXDB['bucket']
        self.write_api = self.client.write_api()
        self.query_api = self.client.query_api()

    def write_data(self, measurement, field_name, field_value, tags=None):
        """
        InfluxDB에 데이터 쓰기
        :param measurement: 측정 이름
        :param field_name: 필드 이름 (예: "temperature")
        :param field_value: 필드 값 (예: 25.3)
        :param tags: dict 형태의 태그 데이터 (옵션)
        """
        point = Point(measurement).field(field_name, field_value)
        if tags:
            for key, value in tags.items():
                point = point.tag(key, value)
        self.write_api.write(bucket=self.bucket, record=point)

    def query_data(self, flux_query):
        """
        InfluxDB에서 데이터 조회
        :param flux_query: FluxQL 쿼리
        :return: 조회 결과
        """
        return self.query_api.query(flux_query)

    def close(self):
        """클라이언트 종료"""
        self.client.close()

def log_temperature(temperature):
    influx_handler = InfluxDBHandler()
    influx_handler.write_data(
        measurement="temperature",
        field_name="value",
        field_value=temperature
    )
    influx_handler.close()

def log_illuminance(illuminance):
    influx_handler = InfluxDBHandler()
    influx_handler.write_data(
        measurement="illuminance",
        field_name="value",
        field_value=illuminance
    )
    influx_handler.close()