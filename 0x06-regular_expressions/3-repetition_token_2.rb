#!/usr/bin/env ruby

string = ARGV[0]
matches = string.scan(/hbtt?t?t?n/)
if matches.any?
  puts matches
else
  puts ""
end
