import sys

total_size = 0
count_by_status = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
lines_processed = 0

try:
  for line in sys.stdin:
    # Split the line into fields
    fields = line.split()
    # Extract file size and status code
    file_size = int(fields[-1])
    status_code = int(fields[-2])

    # Update metrics
    total_size += file_size
    count_by_status[status_code] += 1

    # Print statistics every 10 lines
    if (lines_processed % 10) == 0:
      print(f"File size: {total_size}")
      for status_code, count in sorted(count_by_status.items()):
        if count > 0:
          print(f"{status_code}: {count}")

    lines_processed += 1

except KeyboardInterrupt:
  # Handle keyboard interrupt (CTRL+C)
  print(f"\nFile size: {total_size}")
  for status_code, count in sorted(count_by_status.items()):
    if count > 0:
      print(f"{status_code}: {count}")