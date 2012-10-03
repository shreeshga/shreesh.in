.PHONY: generate preview publish

# We extend PYTHONPATH to include the current directory so that settings
# inclusion will work well.
export PYTHONPATH := .:${PYTHONPATH}

# Run the preview webserver on port 8000
PREVIEW_PORT=8000

PREVIEW_URL=http://localhost:${PREVIEW_PORT}/

preview:
	env FIRMANT_OUTPUT_DIR=preview \
		FIRMANT_PERMALINK_ROOT=${PREVIEW_URL} \
		firmant settings
	@echo
	@echo "Starting local server. ^C to kill it (Control + C)"
	@echo "Visit: ${PREVIEW_URL}"
	cd preview && python -m SimpleHTTPServer

publish:
	env FIRMANT_OUTPUT_DIR=shreesh.in \
		FIRMANT_PERMALINK_ROOT=http://shreesh.in/\
		firmant settings
	#rsync -PLrvhz --chmod=ugo=rwX --delete --exclude='\.*' shreesh.in/ "oml@oml.in:/home/oml/shreesh/"
	rsync -e "ssh -i /Users/shreeshga/Keys/servertype.pem" -PLrvhz --chmod=ugo=rwX --delete --exclude='\.*' shreesh.in/ "ubuntu@54.245.116.120:/home/ubuntu/shreesh.in/blog/"
