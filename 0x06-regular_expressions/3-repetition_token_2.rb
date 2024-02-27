#!/usr/bin/env ruby

string = ARGV[0]
matches = string.scan(/hbt+n/)
if matches.any?
  puts matches
else
  puts ""
end
