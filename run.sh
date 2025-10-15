#!/usr/bin/env bash
VERSION="3cba7d7"
container run \
	--rm \
	-v $(pwd):/workspace \
	-v $HOME/sesh/$SESH/output_user_root:/output_user_root \
	-v $HOME/sesh/$SESH/cache:/root/.cache \
	buildbox:$VERSION \
	"$@"
