#!/usr/bin/env ruby

string = ARGV[0]
matches = string.scan(/[A-Z]/)
if matches.any?
  print matches.join
  puts ""
else
  puts ""
end
