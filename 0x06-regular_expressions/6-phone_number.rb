#!/usr/bin/env ruby

laTelephone = ARGV[0]
match = /^\d{10}$/
if laTelephone =~ match
  puts match
else
  puts ""
end
