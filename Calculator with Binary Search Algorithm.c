/* calculator.c */

/* author: Michael Nguyen */


/* Pseudo Code

1) create an option menu with printf() and have intro outside of loop so it does not repeat and use
   scanf() for user input (done)
2) allow user selections with switch statements. Before, if user inputs 0, program should quit first (done)
3) initialize variables accordingly with floats and ints (done)
4) hold a current result to be used with other calculations (done)
5) error handling (done)
6) let selection and new_value be equal to 0 in the beginning so that the value can be displayed properly and be
   used for calculations from the beginning (done)

*/


#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* initialize functions */

double Add(double op1, double op2)
{
    double sum;
    sum = op1+op2;
    return sum;
}

double Subtract(double op1, double op2)
{
    double sub;
    sub = op1 - op2;
    return sub;
}

double Multiply(double op1, double op2)
{
    double mult;
    mult = op1*op2;
    return mult;
}

double Divide(double op1, double op2)
{
    double div;
    div = op1/op2;
    return div;
}

double Abs(double op1)
{
    return (op1 < 0) ? (-op1) : (op1);
}

double ApproximateRoot2(double op1)
{
    int range, counter = 1;
    double M, L, R, N, current_result, range_diff;
    
    L = 0;
    R = op1;
    N = op1;
    
    M = L + (R-L)/2;

    for(range = 0; range >= 0; counter++)
    {  
        if ((M*M)<N)    /*use middle-to-right */
        {
            range_diff = R - L;

            if (range_diff < 0.000001)
            {
                printf("\nIteration %d: the square root of %.6f is approximately %.6f\n", counter, op1, M);
                current_result = M;
                break;
            }
            
            printf("\nIteration %d: the square root of %.6f is approximately %.6f\n", counter, op1, M);
            
            L = M;
            M = L + (R-L)/2;                                 
        }

        else    /* use left-to-middle */
        {
            range_diff = R - L;

            if (range_diff < 0.000001)
            {
                printf("\nIteration %d: the square root of %.6f is approximately %.6f\n", counter, op1, M);
                current_result = M;
                break;
            }
            
            printf("\nIteration %d: the square root of %.6f is approximately %.6f\n", counter, op1, M);
            
            R = M;
            M = L + (R-L)/2;  
        }
    
    } /* end of for loop */

    return current_result; 
}


double ApproximateRootN(double op1, unsigned int n)
{
    int range, counter = 1, i = 2;
    double M, L, R, N, current_result, base, const_value_M;
    
    L = 0;
    R = op1;
    N = op1;
    
    M = L + (R-L)/2;

    for(range = 0; range >= 0; counter++)
    {  
        base = M;
        const_value_M = M;
        
        while(i<=n)
        {
            base = base*const_value_M;
            i++;    /* start at a value of 2 because multiplication already occurs */ 
        }
        
        if (base<N)    /*use middle-to-right */
        {
            if (base == op1)
            {
                printf("\nIteration %d: the %dth root of %.6f is approximately %.6f\n", counter, n, op1, M);
                current_result = M;
                break;
            }
            
           if (counter >= 50)  /* I found that at this counter the result is constant throughout */ 
            {
                printf("\nIteration %d: the %dth root of %.6f is approximately %.6f\n", counter, n, op1, M);
                current_result = M;
                break;
            }

            printf("\nIteration %d: the %dth root of %.6f is approximately %.6f\n", counter, n, op1, M);
            
            L = M;
            M = L + (R-L)/2;   
            i = 2;             /* set value back to 2 to check the loop again */                       
        }

        else    /* use left-to-middle */
        {
            if (base == op1)
            {
                printf("\nIteration %d: the %dth root of %.6f is approximately %.6f\n", counter, n, op1, M);
                current_result = M;
                break;
            }
            
            if (counter >= 50)      /* I found that at this counter the result is constant throughout */ 
            {
                printf("\nIteration %d: the %dth root of %.6f is approximately %.6f\n", counter, n, op1, M);
                current_result = M;
                break;
            }

            printf("\nIteration %d: the %dth root of %.6f is approximately %.6f\n", counter, n, op1, M);
            
            R = M;
            M = L + (R-L)/2;  
            i = 2;        /* set value back to 2 to check the loop again */  
        }
    
    } /* end of for loop */

    return current_result; 
}


/* main function */

int main(void)

{
    /* initialize variables */

    int selection = 0, N;
    double new_value = 0.0, add_value, subtract_value, multiply_value, divide_value;
    double choice_1, choice_2, choice_3, choice_4, choice_5, choice_6, choice_7, choice_8, choice_9, choice_10;


    /* create the option menu */

    printf("Welcome to my calculator!\n");
    printf("--------------------------------------------\n");
    printf("Current result: %d\n", selection);
    printf("--------------------------------------------\n");

    while(-1)
    {  
        printf(" 0. Enter a new current value\n");
        printf(" 1. Add a number to the current result\n");
        printf(" 2. Subtract a number from the current result\n");
        printf(" 3. Multiply the current result by a number\n");
        printf(" 4. Divide the current result by a number\n");
        printf(" 5. Calculate the absolute value of the current result\n");
        printf(" 6. Calculate the sine of the current result\n");
        printf(" 7. Calculate the cosine of the current result\n");
        printf(" 8. Calculate the tangent of the current result\n");
        printf(" 9. Calculate the square root of the current result\n");
        printf("10. Calculate the Nth of the current result\n");
        printf("11. Quit\n\n");

        printf("Please enter your selection: ");
        scanf("%d", &selection);
       
        switch (selection)
        {
            case 11:
            {
                printf("\n");
                exit(0);        /* 0 represents successful exit, any non integer is an error */
            }
        
            case 0:
            {
                printf("Please enter the new value: ");
                scanf("%lf", &new_value);
                printf("\n--------------------------------------------\n");
                printf("Current result: %g", new_value);
                printf("\n--------------------------------------------\n\n");
                break;
            }

            case 1:
            {
                printf("Please enter the summand: ");
                scanf("%lf", &add_value);
                choice_1 = Add(add_value, new_value);
                printf("\n--------------------------------------------\n");
                printf("Current result: %g", choice_1);
                printf("\n--------------------------------------------\n\n");
                new_value = choice_1;
                break;
            }
            
            case 2: 
            {
                printf("Please enter a number to subtract from the previous value: ");
                scanf("%lf", &subtract_value);
                choice_2 = Subtract(new_value, subtract_value);
                printf("\n--------------------------------------------\n");
                printf("Current result: %g", choice_2);
                printf("\n--------------------------------------------\n\n");
                new_value = choice_2;
                break;
            }

            case 3:
            {
                printf("Please enter the factor: ");
                scanf("%lf", &multiply_value);
                choice_3 = Multiply(multiply_value, new_value);
                printf("\n--------------------------------------------\n");
                printf("Current result: %g", choice_3);
                printf("\n--------------------------------------------\n\n");
                new_value = choice_3;
                break;
            }

            case 4:
            {
                printf("Please enter the divisor: ");
                scanf("%lf", &divide_value);
                choice_4 = Divide(new_value, divide_value);
                
                if (divide_value == 0)
                {
                    printf("\nERROR: Division by zero!\n\n");     /* error handling for div by 0 */
                    break;
                }
               
                printf("\n--------------------------------------------\n");
                printf("Current result: %g", choice_4);
                printf("\n--------------------------------------------\n\n");
                new_value = choice_4;
                break;
            }

             case 5:
            {
                choice_5 = Abs(new_value);
                printf("\n--------------------------------------------\n");
                printf("Current result: %g", choice_5);
                printf("\n--------------------------------------------\n\n");
                new_value = choice_5;
                break;
            }

              case 6:
            {
                choice_6 = sin(new_value);
                printf("\n--------------------------------------------\n");
                printf("Current result: %g", choice_6);
                printf("\n--------------------------------------------\n\n");
                new_value = choice_6;
                break;
            }

               case 7:
            {
                choice_7 = cos(new_value);
                printf("\n--------------------------------------------\n");
                printf("Current result: %g", choice_7);
                printf("\n--------------------------------------------\n\n");
                new_value = choice_7;
                break;
            }

               case 8:
            {
                if (new_value <= -1.3 || new_value >= 1.3)
                {
                    printf("\nERROR: Input out of range!\n\n");   /* error handling with tangent range */ 
                    break;
                }
                
                choice_8 = tan(new_value);
                printf("\n--------------------------------------------\n");
                printf("Current result: %g", choice_8);
                printf("\n--------------------------------------------\n\n");
                new_value = choice_8;
                break;
            }

               case 9:
            {               
                if (new_value < 0)
                {
                    printf("ERROR: Root of a negative number!\n");  /* error handling with sqrt of value < 0 */
                    break;
                }

                choice_9 = ApproximateRoot2(new_value);
                printf("\n--------------------------------------------\n");
                printf("Current result: %g", choice_9);
                printf("\n--------------------------------------------\n\n");
                new_value = choice_9;
                break;
            }

                case 10:
            {   
                if (new_value < 0)
                {
                    printf("\nERROR: Root of a negative number!\n\n");
                    break;
                }
                
                printf("Please input the value of integer N: ");
                scanf("%d", &N);   

                if (N <= 0)
                {
                    printf("\nERROR: Invalid integer N!\n\n");
                    break;
                }        
                
                choice_10 = ApproximateRootN(new_value, N);
                printf("\n--------------------------------------------\n");
                printf("Current result: %g", choice_10);
                printf("\n--------------------------------------------\n\n");
                new_value = choice_10;
                break;
            }
        
        } /* end of switch */

    } /* end of while */

    return 0;
}

/* EOF */
