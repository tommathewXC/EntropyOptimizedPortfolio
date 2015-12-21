#pragma once
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <boost\tokenizer.hpp>
#include <boost\foreach.hpp>
#include <map>
#include <math.h>

using namespace			std;
using namespace			boost;

extern const int		R = 1260;
extern const string		TRAINING_DIR = "C:\\Users\\Public\\Documents\\Stephy files\\NJIT\\Fall 2015\\Project\\training\\";
extern const string		TESTING_DIR = "C:\\Users\\Public\\Documents\\Stephy files\\NJIT\\Fall 2015\\Project\\testing\\";
extern bool				CONSOLE_PRINT = false;
int						roundDownNear(double a, int b);
void					getPDFs();
int						rowCount(string filename);

/// <summmary> 
/// Thie method takes a double value as input, and a binning size integer. Then it rounds the double numeric down to the lowest closes
/// multiple of the binning size
/// <param name="value_to_round"> This is the input value that is to be rounded down to the nearest binning mutiple</param>
/// <param name="integral_binning_size"> This is precision at which the probability distribution builder bins the data. Currently only supports integral binning sizes</param></summmary>

int						roundDownNear(double value_to_round, int integral_binning_size)
{
	if (value_to_round <= 0 || integral_binning_size <= 0 || integral_binning_size > value_to_round)
	{
		return 0;
	}

	else
	{
		int rem = ((int)value_to_round) % integral_binning_size;
		return (int)(value_to_round - rem);
	}
}



void					getPDFs(string FILE_NAME, int BINNING_INTERVAL)
{
	//FIELDS

	string path = TRAINING_DIR + FILE_NAME;						// file name
	ifstream _INPUT_FILE_STREAM;								// file stream
	string line;												// string to hold line
	int i = 0;													// counter for
	double _minimum = 10000;
	double _maximum = -1;
	double SUM = 0;
	string FN = FILE_NAME;
	string PDF_PATH;

	int ROWS_IN_TABLE = rowCount(TRAINING_DIR + FILE_NAME);

	std::vector<double> X(ROWS_IN_TABLE - 1);
	std::vector<int> binned_X(ROWS_IN_TABLE - 1);
	std::vector<int> binned_X2(ROWS_IN_TABLE - 1);
	string::size_type loc = FN.find("TABLE_");
	if (loc != string::npos)
	{
		FN.erase(loc, 6);
	}
	PDF_PATH = TRAINING_DIR + "_PDF_BIN_" + to_string(BINNING_INTERVAL) + "_" + FILE_NAME;
	// PROCEDURES

	_INPUT_FILE_STREAM.open(path);								// create file stream from path
	while (getline(_INPUT_FILE_STREAM, line, '\n'))
	{
		char_separator<char> sep(",");
		tokenizer<char_separator<char>> tokens(line, sep);
		int x = 0;
		BOOST_FOREACH(const string& t, tokens)
		{
			x++;
			if (x == 5)
			{
				if (i > 0)
				{
					double v = stod(t);
					binned_X[i - 1] = roundDownNear(v, BINNING_INTERVAL);
					binned_X2[i - 1] = roundDownNear(v, BINNING_INTERVAL);
					if (v > _maximum)
					{
						_maximum = v;
					}
					if (v < _minimum)
					{
						_minimum = v;
					}
					SUM += v;
				}
			}
		}
		i++;
	}
	_INPUT_FILE_STREAM.close();
	std::sort(binned_X.begin(), binned_X.end());
	auto L = unique(binned_X.begin(), binned_X.end());
	binned_X.erase(L, binned_X.end());
	int reduced_size = binned_X.size();
	std::vector<int> RUNNING_COUNT(reduced_size);

	for (int _i = 0; _i < reduced_size; _i++)
	{
		RUNNING_COUNT[_i] = count(binned_X2.begin(), binned_X2.end(), binned_X[_i]);

		if (CONSOLE_PRINT)
		{
			cout << binned_X[_i] << " occured " << RUNNING_COUNT[_i] << " times." << endl;
		}

	}

	ofstream output(PDF_PATH);
	output << "Value,Frequency" << endl;
	for (int q = 0; q < reduced_size; q++)
	{
		output << to_string(binned_X[q]) + "," + to_string(RUNNING_COUNT[q]) << endl;
	}
	output.close();
}


int						rowCount(string filename)
{
	int num_lines = 0;
	string l;
	ifstream myfile(filename);
	while (std::getline(myfile, l))
	{
		num_lines++;
	}
	return num_lines;
}