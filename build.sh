#!/usr/bin/env bash
# -*- coding: utf-8 -*-

#####################################################
# Main
function main() {
	local -r THIS_DIR="$(cd $(dirname $BASH_SOURCE); pwd)"
	
	
	docker image build -t  abcbank/apiv1:latest ${THIS_DIR}/apiv1
	docker image build -t  abcbank/web:latest ${THIS_DIR}/web
	docker image build -t  abcbank/custinfo:latest ${THIS_DIR}/custinfo

	docker image push abcbank/apiv1:latest
	docker image push abcbank/web:latest
	docker image push abcbank/custinfo:latest
}

set -e
main "$@"
