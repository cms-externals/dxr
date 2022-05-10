CFLAGS	:= -Ire2/ -I$(SQLITE_ROOT)/include -Wall -fPIC -ansi -fcommon
LDFLAGS := -Lre2/obj -lre2 -L$(SQLITE_ROOT)/lib -lsqlite3 -shared
SOURCES := kmp.c scanstr.c varint.c hash.c expr.c match.c regexp.cpp cursor.c vtable.c trilite.c
OBJECTS := $(patsubst %.cpp,%.o,$(patsubst %.c,%.o,$(SOURCES))) 
all: debug
debug: CFLAGS += -g
debug: libtrilite.so
release: CFLAGS += -DNDEBUG -O3
release: LDFLAGS += -O3
release: libtrilite.so
re2/obj/libre2.a:
	$(MAKE) -C re2 CXXFLAGS='-Wall -O3 -pthread -fPIC' obj/libre2.a
%.o: %.cpp
	$(CXX) $(CFLAGS) -c $< -o $@
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@
libtrilite.so: $(OBJECTS) re2/obj/libre2.a
	$(CXX) $(OBJECTS) $(LDFLAGS) -o $@
check: all
	cat test.sql | sqlite3 -bail; \
	if [ "$$?" -eq "0" ]; then \
		echo "Test passed"; \
	else \
		echo "Test failed!"; \
	fi
clean:
	rm -rf libtrilite.so $(OBJECTS)
dist-clean:
	rm -rf libtrilite.so $(OBJECTS) re2/
