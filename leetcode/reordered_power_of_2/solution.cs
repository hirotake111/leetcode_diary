using System.Collections.Generic;
using System;
using System.Linq;

public class Solution
{
    public bool ReorderedPowerOf2(int n)
    {
        string Order(int m) => new string(m.ToString().ToCharArray().OrderBy(c => c).ToArray());
        string target = Order(n);
        for (int i = 1; i < int.MaxValue; i *= 2)
        {
            string candidate = Order(i);
            if (target == candidate)
                return true;
            if (target.Length < candidate.Length)
                return false;
        }
        return false;
    }
}
