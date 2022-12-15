{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'numpy'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[39mimport\u001b[39;00m \u001b[39mnumpy\u001b[39;00m \u001b[39mas\u001b[39;00m \u001b[39mnp\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[39mfrom\u001b[39;00m \u001b[39mmatplotlib\u001b[39;00m \u001b[39mimport\u001b[39;00m pyplot \u001b[39mas\u001b[39;00m plt\n\u001b[0;32m      4\u001b[0m ys \u001b[39m=\u001b[39m \u001b[39m200\u001b[39m \u001b[39m+\u001b[39m np\u001b[39m.\u001b[39mrandom\u001b[39m.\u001b[39mrandn(\u001b[39m100\u001b[39m)\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'numpy'"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from matplotlib import pyplot as plt\n",
    "\n",
    "ys = 200 + np.random.randn(100)\n",
    "x = [x for x in range(len(ys))]\n",
    "\n",
    "plt.plot(x, ys, '-')\n",
    "plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)\n",
    "\n",
    "plt.title(\"Sample Visualization\")\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "f3cb1b36911b8b817348a92b8ab2bcaff1c1896763050e785132577c5e6e4cd8"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
