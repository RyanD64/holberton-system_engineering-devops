![alt text](https://s3.amazonaws.com/lowres.cartoonstock.com/business-commerce-mouse-computer_rage-angry-crashed_computer-works-bstn730_low.jpg)

I was working on my server containing three websites and one load balancer when I notice than the loading time of my websites are significantly slower than usual, I firstly checked if the problem came from my computer and after thirty minutes of standing here doing non-conclusive work, I tried to access to the load balancer until I realize that I cannot access to the load balancer.

I tried two or three more times until I remember doing ONE big mistake, I configured the firewalls to restrict all ports except the 443 and I also denied it at the same time. This basi
cally meant than I couldn't access my load balancer at all.

The consequences were 2 hours wasted due to the making of a new load balancer and testing it(no one wants something that does NOT work) so that brings the total time wasted at two hours and a half and two good lessons:
One: always be careful about what you're doing
Two: always make back-ups

Here's the recapitlulation of the incident:

20h00: logging in my computer
20h03: checking the websites(and seeing the loadnig problem)
20h05: checking the task monitor
20h10: trying to free memory in order to make loading time quicker
20h20: trying solutions on the internet and browser entensions
20h32: the three trials to connect to the load balancer(all fails)
20h44: beginning of the creation of a new load balancer
21h22: beginning of the testing of the new load balancer
22h12: thourough verification to ensure that no errors are left
22h25: releasing of the new load balancer
22h30: return to normal
  
In the hope that no one else reading this will do the same mistakes