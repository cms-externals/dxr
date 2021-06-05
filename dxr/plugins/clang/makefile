CLANG_LIBS := -lclang
LLVM_CONFIG ?= llvm-config
LLVM_LDFLAGS := $(shell ${LLVM_CONFIG} --ldflags --libs --system-libs) $(CLANG_LIBS)
CXXFLAGS := $(shell ${LLVM_CONFIG} --cxxflags) -Wall -Wno-strict-aliasing \
	$(if $(DEBUG),-O0 -g)
LDFLAGS := $(LDFLAGS) -fPIC -g $(LLVM_LDFLAGS) -shared

build: libclang-index-plugin.so

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -fPIC -c $^ -o $@

libclang-index-plugin.so: dxr-index.o sha1.o
	$(CXX) $(LDFLAGS) $^ -o $@

check: build
	which clang
	which clang++

clean:
	$(RM) *.o libclang-index-plugin.so

.PHONY: build clean
