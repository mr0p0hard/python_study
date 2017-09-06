Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 3.5's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/3.5/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               def                 if                  raise
None                del                 import              return
True                elif                in                  try
and                 else                is                  while
as                  except              lambda              with
assert              finally             nonlocal            yield
break               for                 not                 
class               from                or                  
continue            global              pass                

help> raise
The "raise" statement
*********************

   raise_stmt ::= "raise" [expression ["from" expression]]

If no expressions are present, "raise" re-raises the last exception
that was active in the current scope.  If no exception is active in
the current scope, a "RuntimeError" exception is raised indicating
that this is an error.

Otherwise, "raise" evaluates the first expression as the exception
object.  It must be either a subclass or an instance of
"BaseException". If it is a class, the exception instance will be
obtained when needed by instantiating the class with no arguments.

The *type* of the exception is the exception instance's class, the
*value* is the instance itself.

A traceback object is normally created automatically when an exception
is raised and attached to it as the "__traceback__" attribute, which
is writable. You can create an exception and set your own traceback in
one step using the "with_traceback()" exception method (which returns
the same exception instance, with its traceback set to its argument),
like so:

   raise Exception("foo occurred").with_traceback(tracebackobj)

The "from" clause is used for exception chaining: if given, the second
*expression* must be another exception class or instance, which will
then be attached to the raised exception as the "__cause__" attribute
(which is writable).  If the raised exception is not handled, both
exceptions will be printed:

   >>> try:
   ...     print(1 / 0)
   ... except Exception as exc:
   ...     raise RuntimeError("Something bad happened") from exc
   ...
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
   ZeroDivisionError: int division or modulo by zero

   The above exception was the direct cause of the following exception:

   Traceback (most recent call last):
     File "<stdin>", line 4, in <module>
   RuntimeError: Something bad happened

A similar mechanism works implicitly if an exception is raised inside
an exception handler or a "finally" clause: the previous exception is
then attached as the new exception's "__context__" attribute:

   >>> try:
   ...     print(1 / 0)
   ... except:
   ...     raise RuntimeError("Something bad happened")
   ...
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
   ZeroDivisionError: int division or modulo by zero

   During handling of the above exception, another exception occurred:

   Traceback (most recent call last):
     File "<stdin>", line 4, in <module>
   RuntimeError: Something bad happened

Additional information on exceptions can be found in section
*Exceptions*, and information about handling exceptions is in section
*The try statement*.

Related help topics: EXCEPTIONS

help> modules

Please wait a moment while I gather a list of all available modules...

AutoComplete        _pydecimal          enum                pyexpat
AutoCompleteWindow  _pyio               errno               queue
AutoExpand          _random             faulthandler        quopri
Bindings            _sha1               filecmp             random
CallTipWindow       _sha256             fileinput           re
CallTips            _sha512             fnmatch             reprlib
ClassBrowser        _signal             formatter           rlcompleter
CodeContext         _sitebuiltins       fractions           rpc
ColorDelegator      _socket             ftplib              run
Debugger            _sqlite3            functools           runpy
Delegator           _sre                gc                  sched
EditorWindow        _ssl                genericpath         select
FileList            _stat               getopt              selectors
FormatParagraph     _string             getpass             setuptools
GrepDialog          _strptime           gettext             shelve
HyperParser         _struct             glob                shlex
IOBinding           _symtable           gzip                shutil
IdleHistory         _testbuffer         hashlib             signal
MultiCall           _testcapi           heapq               site
MultiStatusBar      _testimportmultiple help                smtpd
ObjectBrowser       _testmultiphase     hmac                smtplib
OutputWindow        _thread             html                sndhdr
ParenMatch          _threading_local    http                socket
PathBrowser         _tkinter            idle                socketserver
Percolator          _tracemalloc        idle_test           sqlite3
PyParse             _warnings           idlelib             sre_compile
PyShell             _weakref            idlever             sre_constants
RemoteDebugger      _weakrefset         imaplib             sre_parse
RemoteObjectBrowser _winapi             imghdr              ssl
ReplaceDialog       abc                 imp                 stat
RstripExtension     aboutDialog         importlib           statistics
ScriptBinding       aifc                inspect             string
ScrolledList        antigravity         io                  stringprep
SearchDialog        argparse            ipaddress           struct
SearchDialogBase    array               itertools           subprocess
SearchEngine        ast                 json                sunau
StackViewer         asynchat            keybindingDialog    symbol
ToolTip             asyncio             keyword             symtable
TreeWidget          asyncore            lib2to3             sys
UndoDelegator       atexit              linecache           sysconfig
WidgetRedirector    audioop             locale              tabbedpages
WindowList          base64              logging             tabnanny
ZoomHeight          bdb                 lzma                tarfile
__future__          binascii            macosxSupport       telnetlib
__main__            binhex              macpath             tempfile
_ast                bisect              macurl2path         test
_bisect             builtins            mailbox             textView
_bootlocale         bz2                 mailcap             textwrap
_bz2                cProfile            marshal             this
_codecs             calendar            math                threading
_codecs_cn          cgi                 mimetypes           time
_codecs_hk          cgitb               mmap                timeit
_codecs_iso2022     chunk               modulefinder        tkinter
_codecs_jp          cmath               msilib              token
_codecs_kr          cmd                 msvcrt              tokenize
_codecs_tw          code                multiprocessing     trace
_collections        codecs              netrc               traceback
_collections_abc    codeop              nntplib             tracemalloc
_compat_pickle      collections         nt                  tty
_compression        colorsys            ntpath              turtle
_csv                compileall          nturl2path          turtledemo
_ctypes             concurrent          numbers             types
_ctypes_test        configDialog        opcode              typing
_datetime           configHandler       operator            unicodedata
_decimal            configHelpSourceEdit optparse            unittest
_dummy_thread       configSectionNameDialog os                  urllib
_elementtree        configparser        parser              uu
_functools          contextlib          pathlib             uuid
_hashlib            copy                pdb                 venv
_heapq              copyreg             pickle              warnings
_imp                crypt               pickletools         wave
_io                 csv                 pip                 weakref
_json               ctypes              pipes               webbrowser
_locale             curses              pkg_resources       winreg
_lsprof             datetime            pkgutil             winsound
_lzma               dbm                 platform            wsgiref
_markerlib          decimal             plistlib            xdrlib
_markupbase         difflib             poplib              xml
_md5                dis                 posixpath           xmlrpc
_msi                distutils           pprint              xxsubtype
_multibytecodec     doctest             profile             zipapp
_multiprocessing    dummy_threading     pstats              zipfile
_opcode             dynOptionMenuWidget pty                 zipimport
_operator           easy_install        py_compile          zlib
_osx_support        email               pyclbr              
_overlapped         encodings           pydoc               
_pickle             ensurepip           pydoc_data          

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> time
Help on built-in module time:

NAME
    time - This module provides various functions to manipulate time values.

DESCRIPTION
    There are two standard representations of time.  One is the number
    of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
    or a floating point number (to represent fractions of seconds).
    The Epoch is system-defined; on Unix, it is generally January 1st, 1970.
    The actual value can be retrieved by calling gmtime(0).
    
    The other representation is a tuple of 9 integers giving local time.
    The tuple items are:
      year (including century, e.g. 1998)
      month (1-12)
      day (1-31)
      hours (0-23)
      minutes (0-59)
      seconds (0-59)
      weekday (0-6, Monday is 0)
      Julian day (day in the year, 1-366)
      DST (Daylight Savings Time) flag (-1, 0 or 1)
    If the DST flag is 0, the time is given in the regular time zone;
    if it is 1, the time is given in the DST time zone;
    if it is -1, mktime() should guess based on the date and time.
    
    Variables:
    
    timezone -- difference in seconds between UTC and local standard time
    altzone -- difference in  seconds between UTC and local DST time
    daylight -- whether local time should reflect DST
    tzname -- tuple of (standard time zone name, DST time zone name)
    
    Functions:
    
    time() -- return current time in seconds since the Epoch as a float
    clock() -- return CPU time since process start as a float
    sleep() -- delay for a number of seconds given as a float
    gmtime() -- convert seconds since Epoch to UTC tuple
    localtime() -- convert seconds since Epoch to local time tuple
    asctime() -- convert time tuple to string
    ctime() -- convert time in seconds to string
    mktime() -- convert local time tuple to seconds since Epoch
    strftime() -- convert time tuple to string according to format specification
    strptime() -- parse string to time tuple according to format specification
    tzset() -- change the local timezone

CLASSES
    builtins.tuple(builtins.object)
        struct_time
    
    class struct_time(builtins.tuple)
     |  The time value as returned by gmtime(), localtime(), and strptime(), and
     |  accepted by asctime(), mktime() and strftime().  May be considered as a
     |  sequence of 9 integers.
     |  
     |  Note that several fields' values are not the same as those defined by
     |  the C language standard for struct tm.  For example, the value of the
     |  field tm_year is the actual year, not year - 1900.  See individual
     |  fields' descriptions for details.
     |  
     |  Method resolution order:
     |      struct_time
     |      builtins.tuple
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  tm_hour
     |      hours, range [0, 23]
     |  
     |  tm_isdst
     |      1 if summer time is in effect, 0 if not, and -1 if unknown
     |  
     |  tm_mday
     |      day of month, range [1, 31]
     |  
     |  tm_min
     |      minutes, range [0, 59]
     |  
     |  tm_mon
     |      month of year, range [1, 12]
     |  
     |  tm_sec
     |      seconds, range [0, 61])
     |  
     |  tm_wday
     |      day of week, range [0, 6], Monday is 0
     |  
     |  tm_yday
     |      day of year, range [1, 366]
     |  
     |  tm_year
     |      year, for example, 1993
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  n_fields = 9
     |  
     |  n_sequence_fields = 9
     |  
     |  n_unnamed_fields = 0
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.n
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __rmul__(self, value, /)
     |      Return self*value.
     |  
     |  count(...)
     |      T.count(value) -> integer -- return number of occurrences of value
     |  
     |  index(...)
     |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
     |      Raises ValueError if the value is not present.

FUNCTIONS
    asctime(...)
        asctime([tuple]) -> string
        
        Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
        When the time tuple is not present, current time as returned by localtime()
        is used.
    
    clock(...)
        clock() -> floating point number
        
        Return the CPU time or real time since the start of the process or since
        the first call to clock().  This has as much precision as the system
        records.
    
    ctime(...)
        ctime(seconds) -> string
        
        Convert a time in seconds since the Epoch to a string in local time.
        This is equivalent to asctime(localtime(seconds)). When the time tuple is
        not present, current time as returned by localtime() is used.
    
    get_clock_info(...)
        get_clock_info(name: str) -> dict
        
        Get information of the specified clock.
    
    gmtime(...)
        gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,
                               tm_sec, tm_wday, tm_yday, tm_isdst)
        
        Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a.
        GMT).  When 'seconds' is not passed in, convert the current time instead.
        
        If the platform supports the tm_gmtoff and tm_zone, they are available as
        attributes only.
    
    localtime(...)
        localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                                  tm_sec,tm_wday,tm_yday,tm_isdst)
        
        Convert seconds since the Epoch to a time tuple expressing local time.
        When 'seconds' is not passed in, convert the current time instead.
    
    mktime(...)
        mktime(tuple) -> floating point number
        
        Convert a time tuple in local time to seconds since the Epoch.
        Note that mktime(gmtime(0)) will not generally return zero for most
        time zones; instead the returned value will either be equal to that
        of the timezone or altzone attributes on the time module.
    
    monotonic(...)
        monotonic() -> float
        
        Monotonic clock, cannot go backward.
    
    perf_counter(...)
        perf_counter() -> float
        
        Performance counter for benchmarking.
    
    process_time(...)
        process_time() -> float
        
        Process time for profiling: sum of the kernel and user-space CPU time.
    
    sleep(...)
        sleep(seconds)
        
        Delay execution for a given number of seconds.  The argument may be
        a floating point number for subsecond precision.
    
    strftime(...)
        strftime(format[, tuple]) -> string
        
        Convert a time tuple to a string according to a format specification.
        See the library reference manual for formatting codes. When the time tuple
        is not present, current time as returned by localtime() is used.
        
        Commonly used format codes:
        
        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.
        
        Other codes may be available on your platform.  See documentation for
        the C library strftime function.
    
    strptime(...)
        strptime(string, format) -> struct_time
        
        Parse a string to a time tuple according to a format specification.
        See the library reference manual for formatting codes (same as
        strftime()).
        
        Commonly used format codes:
        
        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.
        
        Other codes may be available on your platform.  See documentation for
        the C library strftime function.
    
    time(...)
        time() -> floating point number
        
        Return the current time in seconds since the Epoch.
        Fractions of a second may be present if the system clock provides them.

DATA
    altzone = -10800
    daylight = 1
    timezone = -7200
    tzname = ('\xd4\xb3\xed\xeb\xff\xed\xe4\xb3\xff (\xe7\xe8\xec\xe0)', '\xd4\xb3\xed\xeb\xff\xed\xe4\xb3\xff (\xeb\xb3\xf2\xee)')

FILE
    (built-in)


help> exit
Help on Quitter in module _sitebuiltins object:

exit = class Quitter(builtins.object)
 |  Methods defined here:
 |  
 |  __call__(self, code=None)
 |      Call self as a function.
 |  
 |  __init__(self, name, eof)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

help> restart
No Python documentation found for 'restart'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> dev
No Python documentation found for 'dev'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
>>> hex(260)
'0x104'
>>> bin(260)
'0b100000100'
>>> oct(260)
'0o404'
>>> int(0x104)
260
>>> hex(505)
'0x1f9'
>>> int(ob100000100)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    int(ob100000100)
NameError: name 'ob100000100' is not defined
>>> int(0b100000100)
260
>>> '0b100000100'
'0b100000100'
>>> 0b100000100
260
>>> 2+2
4
>>> sin(30)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    sin(30)
NameError: name 'sin' is not defined
>>> 3*826345
2479035
>>> c = 150
>>> d = 12.9
>>> c+d
162.9
>>> p=abs(d-c)
>>> print(p)
137.1
>>> round(p)
137
>>> import math
>>> math pi
SyntaxError: invalid syntax
>>> math.pi
3.141592653589793
>>> math.sqrt(64)
8.0
>>> math.sin(30)
-0.9880316240928618
>>> math.sin(90)
0.8939966636005579
>>> s='spam'
>>> s=s[0]+
SyntaxError: invalid syntax
>>> s=s[0]+'b'+s[2:]
>>> s
'sbam'
>>> len('Богдан Сергійович Кусьо')
23
>>> c=[c*5 for c in 'diisk')
SyntaxError: invalid syntax
>>> c=[c*5 for c in 'diisk']
>>> c
['ddddd', 'iiiii', 'iiiii', 'sssss', 'kkkkk']
>>> c=[c+d for c in 'list' if c!-'i' for d in 'spam' if d!='a']
SyntaxError: invalid syntax
>>> c=[c+d for c in 'list' if c!='i' for d in 'spam' if d!='a']
>>> c
['ls', 'lp', 'lm', 'ss', 'sp', 'sm', 'ts', 'tp', 'tm']
>>> d=[d+a+b+c for d in 'math' if d!='a' for a in 'spam' a!='a' for b in 'nyx' for c in 'dream' if c!='a']
SyntaxError: invalid syntax
>>> d=[d+a+b+c for d in 'math' if d!='a' for a in 'spam' if a!='a' for b in 'nyx' for c in 'dream' if c!='a']
>>> d
['msnd', 'msnr', 'msne', 'msnm', 'msyd', 'msyr', 'msye', 'msym', 'msxd', 'msxr', 'msxe', 'msxm', 'mpnd', 'mpnr', 'mpne', 'mpnm', 'mpyd', 'mpyr', 'mpye', 'mpym', 'mpxd', 'mpxr', 'mpxe', 'mpxm', 'mmnd', 'mmnr', 'mmne', 'mmnm', 'mmyd', 'mmyr', 'mmye', 'mmym', 'mmxd', 'mmxr', 'mmxe', 'mmxm', 'tsnd', 'tsnr', 'tsne', 'tsnm', 'tsyd', 'tsyr', 'tsye', 'tsym', 'tsxd', 'tsxr', 'tsxe', 'tsxm', 'tpnd', 'tpnr', 'tpne', 'tpnm', 'tpyd', 'tpyr', 'tpye', 'tpym', 'tpxd', 'tpxr', 'tpxe', 'tpxm', 'tmnd', 'tmnr', 'tmne', 'tmnm', 'tmyd', 'tmyr', 'tmye', 'tmym', 'tmxd', 'tmxr', 'tmxe', 'tmxm', 'hsnd', 'hsnr', 'hsne', 'hsnm', 'hsyd', 'hsyr', 'hsye', 'hsym', 'hsxd', 'hsxr', 'hsxe', 'hsxm', 'hpnd', 'hpnr', 'hpne', 'hpnm', 'hpyd', 'hpyr', 'hpye', 'hpym', 'hpxd', 'hpxr', 'hpxe', 'hpxm', 'hmnd', 'hmnr', 'hmne', 'hmnm', 'hmyd', 'hmyr', 'hmye', 'hmym', 'hmxd', 'hmxr', 'hmxe', 'hmxm']
>>> d=[d+a+b+c for d in 'math' if d!='a' for a in 'spam' a!='a' for b in 'nyx' for c in 'dream' if c!='a' and c!='e']
SyntaxError: invalid syntax
>>> d=[d+a+b+c for d in 'math' if d!='a' for a in 'spam' in a!='a' for b in 'nyx' for c in 'dream' if c!='a' and c!='e']
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    d=[d+a+b+c for d in 'math' if d!='a' for a in 'spam' in a!='a' for b in 'nyx' for c in 'dream' if c!='a' and c!='e']
  File "<pyshell#42>", line 1, in <listcomp>
    d=[d+a+b+c for d in 'math' if d!='a' for a in 'spam' in a!='a' for b in 'nyx' for c in 'dream' if c!='a' and c!='e']
UnboundLocalError: local variable 'a' referenced before assignment
>>> d=[d+a+b+c for d in 'math' if d!='a' for a in 'spam' in a!='a' for b in 'nyx' for c in 'dream' if c!='ea']
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    d=[d+a+b+c for d in 'math' if d!='a' for a in 'spam' in a!='a' for b in 'nyx' for c in 'dream' if c!='ea']
  File "<pyshell#43>", line 1, in <listcomp>
    d=[d+a+b+c for d in 'math' if d!='a' for a in 'spam' in a!='a' for b in 'nyx' for c in 'dream' if c!='ea']
UnboundLocalError: local variable 'a' referenced before assignment
>>> d=[d+a+b+c for d in 'math' if d!='a' for a in 'spam' if a!='a' for b in 'nyx' for c in 'dream' if c!='a' and c!='e']
>>> d
['msnd', 'msnr', 'msnm', 'msyd', 'msyr', 'msym', 'msxd', 'msxr', 'msxm', 'mpnd', 'mpnr', 'mpnm', 'mpyd', 'mpyr', 'mpym', 'mpxd', 'mpxr', 'mpxm', 'mmnd', 'mmnr', 'mmnm', 'mmyd', 'mmyr', 'mmym', 'mmxd', 'mmxr', 'mmxm', 'tsnd', 'tsnr', 'tsnm', 'tsyd', 'tsyr', 'tsym', 'tsxd', 'tsxr', 'tsxm', 'tpnd', 'tpnr', 'tpnm', 'tpyd', 'tpyr', 'tpym', 'tpxd', 'tpxr', 'tpxm', 'tmnd', 'tmnr', 'tmnm', 'tmyd', 'tmyr', 'tmym', 'tmxd', 'tmxr', 'tmxm', 'hsnd', 'hsnr', 'hsnm', 'hsyd', 'hsyr', 'hsym', 'hsxd', 'hsxr', 'hsxm', 'hpnd', 'hpnr', 'hpnm', 'hpyd', 'hpyr', 'hpym', 'hpxd', 'hpxr', 'hpxm', 'hmnd', 'hmnr', 'hmnm', 'hmyd', 'hmyr', 'hmym', 'hmxd', 'hmxr', 'hmxm']
>>> 
