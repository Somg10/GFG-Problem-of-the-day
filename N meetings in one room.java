class EndSorter implements Comparator<meeting>
{
	@Override
	//Sorting meetings based on finish timings
	public int compare(meeting o1, meeting o2) 
	{
		if (o1.end < o2.end)
			return -1;
		
		else if (o1.end > o2.end)
		 	return 1;
			
		return 0;
	}
}

 
class meeting
{
	int start;
	int end;
	int pos;
	// Constructor to create meeting(start,end,position) pairs
	meeting(int start, int end, int pos)
	{
		this.start = start;
		this.end = end;
		this.pos = pos;
	}
}

class Solution {
    public static int maxMeetings(int start[], int end[], int n)
    {   
        ArrayList<meeting> pair = new ArrayList<>();
        for(int i = 0; i < n; i++){	
		pair.add(new meeting(start[i], end[i], i));
	     }
     ArrayList<Integer> m = new ArrayList<>();
    
	int c = 1;
	
	EndSorter es = new EndSorter(); 
	Collections.sort(pair, es);
  m.add(pair.get(0).pos);
	int prev_end = pair.get(0).end;
	for(int i = 1; i < pair.size(); i++)
	{
		if (pair.get(i).start > prev_end)
		{
			m.add(pair.get(i).pos);
			prev_end = pair.get(i).end;
			c++;
		}
	}
	
	return c;

    }
}
