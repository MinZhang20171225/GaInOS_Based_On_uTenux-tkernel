/*
 *------------------------------------------------------------------------------
 *    Cpu
 *
 *    Copyright (C) 2008-2013 by Dalian uLoong Co.,Ltd. All rights reserved.
 *
 *    This program is open source software; developer can redistribute it and/or
 *    modify it under the terms of the U-License as published by the T-Engine China
 *    Open Source Society; either version 1 of the License, or (at developer option)
 *    any later Version.
 *
 *    This program is distributed in the hope that it will be useful,but WITHOUT ANY
 *    WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
 *    A PARTICULAR PURPOSE.  See the U-License for more details.
 *
 *    Developer should have received a copy of the U-License along with this program;
 *    if not, download from www.tecoss.org(the web page of the T-Engine China Open
 *    Source Society).
 *
 *    CPU:        MC9S12
 *    RTOS:       uT-Kernel
 *    Version:    1.4.00
 *    Released by T-Engine China Open Source Society
 *                  (http://www.tecoss.org).
 *
 *	 File Name      : cpu_status.h
 *	 Create Date    : 2013/3/15-2013/3/17
 *	 Author	        : Fan Wang(parai)
 *	 Description    : CPU-Dependent Definition.
 *-------------------------------------------------------------------------------
 */

#ifndef _CPU_STATUS_
#define _CPU_STATUS_

#include <tk/syslib.h>
#include <tk/sysdef.h>
#include "cpu_insn.h"
/*
 * Interrupt  mask register (Primask)
 */
#define  configUSE_FPU	0
/* Definitions to set the initial MSR of each task. */
#define portCRITICAL_INTERRUPT_ENABLE	( 1UL << 17UL )
#define portEXTERNAL_INTERRUPT_ENABLE	( 1UL << 15UL )
#define portMACHINE_CHECK_ENABLE		( 1UL << 12UL )

#if configUSE_FPU == 1
#define portAPU_PRESENT				( 1UL << 25UL )
#define portFCM_FPU_PRESENT			( 1UL << 13UL )
#else
#define portAPU_PRESENT				( 0UL )
#define portFCM_FPU_PRESENT			( 0UL )
#endif

#define portINITIAL_MSR		( portCRITICAL_INTERRUPT_ENABLE | portEXTERNAL_INTERRUPT_ENABLE | \
                              portMACHINE_CHECK_ENABLE | portAPU_PRESENT | portFCM_FPU_PRESENT )
/*
 * Start/End critical section
 */
#define BEGIN_CRITICAL_SECTION	{ UINT _primask_ = disint();
#define END_CRITICAL_SECTION	if ( !isDI(_primask_)			\
				  && knl_ctxtsk != knl_schedtsk		        	\
				  && !knl_isTaskIndependent()	            	\
				  && !knl_dispatch_disabled ) {		            \
					knl_dispatch();		                    	\
				}				                            	\
				enaint(_primask_); }

/*
 * Start/End interrupt disable section
 */
#define BEGIN_DISABLE_INTERRUPT	{ UINT _primask_ = disint();
#define END_DISABLE_INTERRUPT	enaint(_primask_); }


/*
 * Interrupt enable/disable
 */
#define ENABLE_INTERRUPT	{ enaint(portINITIAL_MSR); }
#define DISABLE_INTERRUPT	{ (void)disint(); }

/*
 * Enable interrupt nesting
 *	Enable the interrupt that has a higher priority than 'level.'
 */
#define ENABLE_INTERRUPT_UPTO(level)	{ (void)enaint(portINITIAL_MSR); }

/*
 * Move to/Restore task independent part
 */
#define ENTER_TASK_INDEPENDENT	{ knl_EnterTaskIndependent(); }
#define LEAVE_TASK_INDEPENDENT	{ knl_LeaveTaskIndependent(); }

/* ----------------------------------------------------------------------- */
/*
 *	Check system state
 */

/*
 * When a system call is called from the task independent part, TRUE
 */
#define in_indp()	( knl_isTaskIndependent() || knl_ctxtsk == NULL )

/*
 * When a system call is called during dispatch disable, TRUE
 * Also include the task independent part as during dispatch disable.
 */
#define in_ddsp()	( knl_dispatch_disabled	\
			|| in_indp()		\
			|| isDI(knl_getPRIMASK()) )

/*
 * When a system call is called during CPU lock (interrupt disable), TRUE
 * Also include the task independent part as during CPU lock.
 */
#define in_loc()	( isDI(knl_getPRIMASK())		\
			|| in_indp() )

/*
 * When a system call is called during executing the quasi task part, TRUE
 * Valid only when in_indp() == FALSE because it is not discriminated from
 * the task independent part.
 */
#define in_qtsk()	( knl_ctxtsk->sysmode > knl_ctxtsk->isysmode )

/* ----------------------------------------------------------------------- */
/*
 *	Task dispatcher startup routine
 */

/*
 * Request for task dispatcher startup
 *	Do nothing at this point because there is no delayed
 *	interrupt function in ARM.
 *	Perform dispatcher startup with END_CRITICAL_SECTION.
 */
#define knl_dispatch_request()	/* */

/*
 * Throw away the current task context.
 * and forcibly dispatch to the task that should be performed next.
 *	Use at system startup and 'tk_ext_tsk, tk_exd_tsk.'
 */
IMPORT void knl_dispatch_to_schedtsk(void); 
#define knl_force_dispatch knl_dispatch_to_schedtsk

/*
 * Start task dispatcher
 */
Inline void knl_dispatch(void)
{
	asm("sc");
}

/* ----------------------------------------------------------------------- */

/*
 * Task context block
 */
typedef struct {
	VP	ssp;		/* System stack pointer */
} CTXB;



#endif /* _CPU_STATUS_ */
