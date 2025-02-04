# priv-subnet-list-gen
Generate list of class C nets in private IP spaces with any exclusions accounted for.

For example, exclude 10.5.x.x, or exclude 10.5.10.x and 10.5.15.x, but generate a /24 line item for every other possible subnet.
- Apply this to a separate list for 10.x.x.x, 172.16.x.x - 172.31.255.x and 192.168.x.x
- lists for each space allow for excluding 10.x.5.x without affecting 192.168.5.x, for example

The output is a list like:
10.0.0.0/24
10.0.1.0/24
etc
