#!/usr/bin/env ruby

laTelephone = ARGV[0]
match = /^\d{10}$/
if (match = laTelephone.match(match))
  puts match
else
  puts ""
end
