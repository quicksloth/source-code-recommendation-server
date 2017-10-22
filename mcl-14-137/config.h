/* config.h.  Generated from config.h.in by configure.  */
/* config.h.in.  Generated from configure.ac by autoheader.  */

/* Predefined possible va_copy() implementation (id: ASP) */
#define __VA_COPY_USE_ASP(d, s) do { *(d) = *(s); } while (0)

/* Predefined possible va_copy() implementation (id: ASS) */
#define __VA_COPY_USE_ASS(d, s) do { (d) = (s); } while (0)

/* Predefined possible va_copy() implementation (id: C99) */
#define __VA_COPY_USE_C99(d, s) va_copy((d), (s))

/* Predefined possible va_copy() implementation (id: CPP) */
#define __VA_COPY_USE_CPP(d, s) memcpy((void *)(d), (void *)(s)), sizeof(*(s))

/* Predefined possible va_copy() implementation (id: CPS) */
#define __VA_COPY_USE_CPS(d, s) memcpy((void *)&(d), (void *)&(s)), sizeof((s))

/* Predefined possible va_copy() implementation (id: GCB) */
#define __VA_COPY_USE_GCB(d, s) __builtin_va_copy((d), (s))

/* Predefined possible va_copy() implementation (id: GCH) */
#define __VA_COPY_USE_GCH(d, s) __va_copy((d), (s))

/* Predefined possible va_copy() implementation (id: GCM) */
#define __VA_COPY_USE_GCM(d, s) VA_COPY((d), (s))

/* Define to 1 if you don't have `vprintf' but do have `_doprnt.' */
#undef HAVE_DOPRNT

/* Define to 1 if you have the <float.h> header file. */
#undef HAVE_FLOAT_H

/* Define to 1 if you have the `floor' function. */
#undef HAVE_FLOOR

/* Define to 1 if you have the <inttypes.h> header file. */
#undef HAVE_INTTYPES_H

/* Define to 1 if you have the `m' library (-lm). */
#undef HAVE_LIBM

/* Define to 1 if you have the <limits.h> header file. */
#undef HAVE_LIMITS_H

/* Define to 1 if your system has a GNU libc compatible `malloc' function, and
   to 0 otherwise. */
#undef HAVE_MALLOC

/* Define to 1 if you have the <malloc.h> header file. */
#undef HAVE_MALLOC_H

/* Define to 1 if you have the <memory.h> header file. */
#undef HAVE_MEMORY_H

/* Define to 1 if you have the `memset' function. */
#undef HAVE_MEMSET

/* Define to 1 if you have the `pow' function. */
#undef HAVE_POW

/* Define if you have POSIX threads libraries and header files. */
#undef HAVE_PTHREAD

/* Define to 1 if you have the `rint' function. */
#undef HAVE_RINT

/* Define to 1 if you have the `sqrt' function. */
#undef HAVE_SQRT

/* Define to 1 if you have the <stdint.h> header file. */
#undef HAVE_STDINT_H

/* Define to 1 if you have the <stdlib.h> header file. */
#undef HAVE_STDLIB_H

/* Define to 1 if you have the `strchr' function. */
#undef HAVE_STRCHR

/* Define to 1 if you have the <strings.h> header file. */
#undef HAVE_STRINGS_H

/* Define to 1 if you have the <string.h> header file. */
#undef HAVE_STRING_H

/* Define to 1 if you have the `strpbrk' function. */
#undef HAVE_STRPBRK

/* Define to 1 if you have the `strstr' function. */
#undef HAVE_STRSTR

/* Define to 1 if you have the <sys/stat.h> header file. */
#undef HAVE_SYS_STAT_H

/* Define to 1 if you have the <sys/types.h> header file. */
#undef HAVE_SYS_TYPES_H

/* Define to 1 if you have the <unistd.h> header file. */
#undef HAVE_UNISTD_H

/* Define if va_copy() macro exists (and no fallback implementation is
   required) */
#undef HAVE_VA_COPY

/* Define to 1 if you have the `vprintf' function. */
#undef HAVE_VPRINTF

/* output citation reference (default yes) */
#undef MCL_HELPFUL_REMINDER

/* Name of package */
#undef PACKAGE

/* Define to the address where bug reports for this package should be sent. */
#undef PACKAGE_BUGREPORT

/* Define to the full name of this package. */
#undef PACKAGE_NAME

/* Define to the full name and version of this package. */
#undef PACKAGE_STRING

/* Define to the one symbol short name of this package. */
#undef PACKAGE_TARNAME

/* Define to the home page for this package. */
#undef PACKAGE_URL

/* Define to the version of this package. */
#undef PACKAGE_VERSION

/* Define to the necessary symbol if this constant uses a non-standard name on
   your system. */
#undef PTHREAD_CREATE_JOINABLE

/* Define to 1 if you have the ANSI C header files. */
#undef STDC_HEADERS

/* Version number of package */
#undef VERSION

/* Optional va_copy() implementation activation */
#ifndef HAVE_VA_COPY
#define va_copy(d, s) __VA_COPY_USE(d, s)
#define HAVE_VA_COPY 1
#endif


/* Define to id of used va_copy() implementation */
#undef __VA_COPY_USE

/* Define to empty if `const' does not conform to ANSI C. */
#undef const

/* Define to rpl_malloc if the replacement function should be used. */
#undef malloc

/* Define to `unsigned int' if <sys/types.h> does not define. */
#undef size_t
