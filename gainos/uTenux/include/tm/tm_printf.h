#ifndef TM_PRINTF_H_H
#define TM_PRINTF_H_H

#include <stdarg.h>

#if 0
#  define TM_PRINTF_PRECISION   /* �Ƿ��ӡС�� */
#  define TM_PRINTF_LONGLONG    /* �Ƿ��ӡ������ */
#  define TM_PRINTF_SPECIAL
#  define TM_TEST_ON_PC
#endif

/* ÿ������ӡ127���ַ� */
#define TM_PRINTF_BUF_SIZE 128
void tm_printf(const char *fmt, ...);

#endif