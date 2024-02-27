#!/usr/bin/env ruby

string = ARGV[0]
matches = string.scan(/hb?tn/)
if matches.any?
  puts matches
else
  puts ""
end
