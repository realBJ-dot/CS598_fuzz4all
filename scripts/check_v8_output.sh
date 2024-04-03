EXECUTION_RES_DIR="v8_fuzz_executed"
mkdir -p $EXECUTION_RES_DIR


FUZZ_DIR="../outputs/js-v8-demo"
LOG_FILE="${FUZZ_DIR}/log_validation.txt"

PATTERN="\[VERBOSE\] outputs/js-v8-demo/\K[^ ]+.fuzz(?= failed validation with error message)"

# Search for the pattern in the file
# Process each matching line

grep -Po "$PATTERN" "$LOG_FILE" | while read -r name; do
    # Extract the filename from the pattern match
    FUZZ_FILE="${name}"
    ORIG_PATH="$FUZZ_DIR/$FUZZ_FILE"
    
    if [ -f "$ORIG_PATH" ]; then
        # Path to the original .fuzz file
        ORIG_PATH="$FUZZ_DIR/$FUZZ_FILE"
        NAME=$(echo "$FUZZ_FILE" | sed 's/\.fuzz$//')

        # Copy the content of [name].fuzz to a new file called test.js
        cp "$ORIG_PATH" test.js

        # Execute test.js with hermes and capture the output
        EXECUTION_OUTPUT=$(/home/v8/v8/output/x64.debug/d8 test.js 2>&1)

        # Write both the content of [name].fuzz and the execution output into [name]_execution
        {
            cat "$ORIG_PATH"
            echo "\n"
	    echo "Execution Output ------------------:"
            echo "$EXECUTION_OUTPUT"
        } > "${EXECUTION_RES_DIR}/fuzz_${NAME}_execution"

        # Optionally, move the execution output file to a specific directory or process it further
        # mv "${NAME}_execution" /path/to/destination/
    else 
	echo "FILE $FUZZ_FILE does not exist"
    fi
done

# clean up
rm test.js
