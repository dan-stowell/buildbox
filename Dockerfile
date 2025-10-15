FROM ubuntu:24.04

RUN \
	apt-get update && apt-get install -y wget && \
	wget "https://github.com/bazelbuild/bazelisk/releases/download/v1.27.0/bazelisk-linux-arm64" && \
	mv bazelisk-linux-arm64 /usr/local/bin/bazel && \
	chmod +x /usr/local/bin/bazel && \
	mkdir -p /workspace \
		/output_user_root \
		/root/.cache && \
	rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
