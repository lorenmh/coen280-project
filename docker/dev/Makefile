INAME=lorenmh/coen281-project
VERSION=0.0.2

all:
	docker build -t $(INAME):latest -t $(INAME):$(VERSION) .
no-cache:
	docker build --no-cache -t $(INAME):latest -t $(INAME):$(VERSION) .
