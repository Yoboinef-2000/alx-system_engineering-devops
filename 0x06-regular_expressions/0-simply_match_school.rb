#!/usr/bin/env ruby

string = ARGV[0]
matches = string.scan(/School/)
if matches.any?
  matches.each do |match|
    print match
  end
  puts ""
else
  puts ""
end
