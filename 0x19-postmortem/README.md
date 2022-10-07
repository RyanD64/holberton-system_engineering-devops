![alt text](https://s3.amazonaws.com/lowres.cartoonstock.com/business-commerce-mouse-computer_rage-angry-crashed_computer-works-bstn730_low.jpg)

I was working on my server containing three websites and one load balancer when I notice than the loading time of my websites are significantly slower than usual, I firstly checked if the problem came from my computer and after thirty minutes of standing here doing non-conclusive work, I tried to access to the load balancer until I realize that I cannot access to the load balancer.

I tried two or three more times until I remember doing ONE big mistake, I configured the firewalls to restrict all ports except the 443 and I also denied it at the same time. This basi
cally meant than I couldn't access my load balancer at all.

The consequences were 2 hours wasted due to the making of a new load balancer and testing it(no one wants something that does NOT work) so that brings the total time wasted at two hours and a half and two good lessons:
One: always be careful about what you're doing
Two: always make back-ups

In the hope that no one else reading this will do the same mistakes