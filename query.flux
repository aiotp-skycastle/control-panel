from(bucket: "influx-bucket")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "temperature")
  |> filter(fn: (r) => r._field == "value")
  |> aggregateWindow(every: v.windowPeriod, fn: mean)
  |> yield(name: "mean")

from(bucket: "influx-bucket")
  |> range(start: -inf, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "temperature")
  |> filter(fn: (r) => r._field == "value")
  |> last()
