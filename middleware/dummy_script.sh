#!/bin/sh

echo "This is a dummy script running in a Docker container!"
echo "Environment Variable: $DUMMY_VARIABLE"

# Keep the container running
tail -f /dev/null
