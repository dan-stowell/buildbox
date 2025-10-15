FROM python:3.14-slim

COPY dan-buildbox.bazelrc /root/.bazelrc
COPY llm-dan-buildbox-tools /llm-dan-buildbox-tools

RUN \
	mkdir -p /workspace && \
	mkdir -p /root/.aider && \
	pip install llm && \
	pip install /llm-dan-buildbox-tools && \
	llm install llm-openrouter && \
	python3 -c "import urllib.request; urllib.request.urlretrieve('https://github.com/bazelbuild/bazelisk/releases/download/v1.27.0/bazelisk-linux-arm64', 'bazelisk')" && \
	mv bazelisk /usr/local/bin/bazelisk && \
	chmod +x /usr/local/bin/bazelisk && \
	pip install aider-chat

ENV \
	LLM_USER_PATH=/workspace/llm_user_path \
	BAZELISK_HOME=/workspace/bazelisk_home

WORKDIR /workspace
